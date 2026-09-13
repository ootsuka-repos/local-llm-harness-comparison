#!/usr/bin/env python3
"""Render the single-page comparison and CSV using only the standard library."""
import argparse
import csv
import hashlib
import io
import json
import re
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LABELS = {
    "start": "起動", "model": "モデル選択", "headless": "非対話実行",
    "resume": "再開", "plan": "計画", "compact": "履歴圧縮",
    "approval": "承認制御", "goal": "目標まで継続", "test": "テスト・修正",
    "delegate": "サブエージェント", "schedule": "定期・背景実行",
    "limits": "実行上限", "sandbox": "隔離", "extend": "拡張・MCP",
    "output": "機械可読出力",
}
KINDS = {"CLI", "SLASH", "CONFIG", "SDK", "EXTENSION", "MODEL", "UI", "UNVERIFIED", "NONE", "MIXED"}
COMMAND_MARKERS = KINDS | {"AGENT LOOP", "UI / SDK", "SDK / EXTERNAL", "EXTERNAL"}
GROUPS = [
    ("基本操作", ["start", "model", "headless", "resume", "plan", "compact"]),
    ("自律運用", ["goal", "test", "delegate", "schedule"]),
    ("実行・拡張", ["approval", "limits", "sandbox", "extend", "output"]),
]
SHORT_LABELS = {**LABELS, "model": "モデル", "headless": "非対話", "compact": "圧縮", "goal": "Goal継続", "test": "テスト", "delegate": "委譲・並列", "schedule": "定期・背景", "approval": "承認", "limits": "上限", "extend": "拡張", "output": "出力"}
KIND_LABELS = {"CLI": "CLI", "SLASH": "対話コマンド", "CONFIG": "設定", "SDK": "SDK", "EXTENSION": "拡張・外部実装", "MODEL": "モデルへの依頼", "UI": "UI", "UNVERIFIED": "未確認", "NONE": "標準なし・別概念", "MIXED": "複数の操作面"}
LOCAL_LABELS = {"supported": "経路あり", "conditional": "条件付き", "unverified": "未確認"}


def inline(value):
    """Escape all HTML; the catalog's only inline markup is backtick code."""
    return ''.join(f'<code>{escape(part)}</code>' if i % 2 else escape(part).replace('\n', '<br>') for i, part in enumerate(re.split(r'`([^`]+)`', value)))


def validate(data):
    sources = data["sources"]
    ids = [h["id"] for h in data["harnesses"]]
    assert len(ids) == len(set(ids)), "duplicate harness id"
    assert len(ids) == 17, "the comparison must show all 17 harnesses"
    assert all(re.fullmatch(r'[a-z0-9-]+', hid) for hid in ids)
    assert data["checked_on"] and sources
    for sid, source in sources.items():
        assert source["url"].startswith("https://"), sid
        assert source["title"] and source["checked_on"], sid
    for h in data["harnesses"]:
        assert h["local"]["status"] in {"supported", "conditional", "unverified"}, h["id"]
        assert h["local"]["sources"], h["id"]
        assert set(h["commands"]) == set(LABELS), h["id"]
        for entry in [h["local"], *h["commands"].values()]:
            assert entry["text"] and entry["sources"], h["id"]
            assert all(s in sources for s in entry["sources"]), h["id"]
        for c in h["commands"].values():
            assert c["kind"] in KINDS
            assert isinstance(c["aliases"], list)
            summary = c['summary']
            assert summary and summary.isascii(), f'{h["id"]}: command cells must not paraphrase syntax in Japanese'
            if summary not in COMMAND_MARKERS:
                assert re.fullmatch(r'`[^`\n]+`', summary), f'{h["id"]}: use literal code or an explicit operation marker'
                reviewed_text = ' '.join([c['text'], *c['aliases']])
                assert summary[1:-1] in reviewed_text, f'{h["id"]}: display syntax must exist in the reviewed entry'
        assert h["notes"] and h["scope"]
        assert h['display_name'] and h['upstream'].startswith('https://')
        assert h['local']['protocol_summary']


def render_page(data):
    sources = data["sources"]
    popovers = []

    def detail(h, key, label, body, source_ids, kind='', aliases=()):
        pid = f'detail-{h["id"]}-{key}'
        links = ''.join(f'<a href="{escape(sources[s]["url"], quote=True)}" target="_blank" rel="noopener noreferrer">{escape(sources[s]["title"])} <span aria-hidden="true">↗</span></a>' for s in source_ids)
        alias_html = ''
        if aliases:
            alias_html = '<div class="detail-aliases"><h3>正式エイリアス</h3>' + ''.join(f'<p>{inline(a)}</p>' for a in aliases) + '</div>'
        kind_html = f'<span class="detail-kind">{escape(kind)}</span>' if kind else ''
        popovers.append(f'''<div class="cell-detail" id="{pid}" popover="auto" role="dialog" aria-labelledby="{pid}-title">
  <button class="close-detail" type="button" popovertarget="{pid}" popovertargetaction="hide" aria-label="詳細を閉じる">×</button>
  <p class="detail-harness">{escape(h['name'])}</p>
  <h2 id="{pid}-title">{escape(label)} {kind_html}</h2>
  <div class="detail-body">{body}</div>{alias_html}
  <div class="detail-sources"><h3>一次資料 · {escape(data['checked_on'])}</h3>{links}</div>
</div>''')
        return pid

    def button(h, key, label, value, pid, css='', title=''):
        return f'<button type="button" class="cell-button {css}" popovertarget="{pid}" aria-label="{escape(h["name"] + "・" + label + "：" + re.sub("`", "", value) + "。詳細を表示", quote=True)}" title="{escape(title, quote=True)}">{inline(value)}</button>'

    groups = ''.join(f'<th scope="colgroup" colspan="{len(keys)}">{name}</th>' for name, keys in GROUPS)
    columns = ''.join(f'<th scope="col" class="{"group-start" if i == 0 else ""}">{SHORT_LABELS[k]}</th>' for _, keys in GROUPS for i, k in enumerate(keys))
    column_groups = ''.join(f'<colgroup><col span="{len(keys)}" class="feature-col"></colgroup>' for _, keys in GROUPS)
    table_head = f'''<colgroup><col class="name-col"></colgroup><colgroup><col class="local-col"><col class="api-col"></colgroup>{column_groups}
<thead><tr class="group-head"><th class="name-head" rowspan="2" scope="col">ハーネス <span class="count">{len(data['harnesses']):02}</span></th><th scope="colgroup" colspan="2">ローカル接続</th>{groups}</tr>
<tr class="column-head"><th scope="col">対応経路</th><th scope="col">API形式</th>{columns}</tr></thead>'''
    rows = []
    for index, h in enumerate(data['harnesses'], 1):
        local = h['local']
        name_body = f'<p>{inline(h["scope"])}</p><ul>' + ''.join(f'<li>{inline(note)}</li>' for note in h['notes']) + f'</ul><a class="official-link" href="{escape(h["upstream"], quote=True)}" target="_blank" rel="noopener noreferrer">公式サイト ↗</a>'
        pid = detail(h, 'scope', '対象・実行面', name_body, local['sources'])
        badge = f'<small class="product-badge">{escape(h["badge"])}</small>' if h['badge'] else ''
        name_button = f'<button type="button" class="name-button" popovertarget="{pid}" aria-label="{escape(h["name"], quote=True)}の対象・実行面"><span class="row-number" aria-hidden="true">{index:02}</span><span class="product-name">{escape(h["display_name"])}{badge}</span><span class="name-arrow" aria-hidden="true">↗</span></button>'
        cells = [f'<th scope="row">{name_button}</th>']
        pid = detail(h, 'local', 'ローカルLLMへの接続', f'<p>{inline(local["text"])}</p>', local['sources'], LOCAL_LABELS[local['status']])
        cells.append('<td class="local-cell">' + button(h, 'local', 'ローカル接続', LOCAL_LABELS[local['status']], pid, 'status-' + local['status'], local['text']) + '</td>')
        pid = detail(h, 'protocol', 'API形式', f'<p>{inline(local["protocol"])}</p><p>{inline(local["text"])}</p>', local['sources'])
        cells.append('<td class="api-cell">' + button(h, 'protocol', 'API形式', local['protocol_summary'], pid, title=local['protocol']) + '</td>')
        for _, keys in GROUPS:
            for i, key in enumerate(keys):
                c = h['commands'][key]
                pid = detail(h, key, LABELS[key], f'<p>{inline(c["text"])}</p>', c['sources'], KIND_LABELS[c['kind']], c['aliases'])
                cell_css = 'group-start ' if i == 0 else ''
                cells.append(f'<td class="{cell_css}kind-{c["kind"].lower()}">' + button(h, key, LABELS[key], c['summary'], pid, title=c['text']) + '</td>')
        rows.append(f'<tr id="{h["id"]}">' + ''.join(cells) + '</tr>')
    template = (ROOT / 'site/template.html').read_text()
    replacements = {
        'CHECKED_ON': escape(data['checked_on']), 'COUNT': str(len(data['harnesses'])),
        'ASSET_VERSION': hashlib.sha256((ROOT / 'assets/style.css').read_bytes() + (ROOT / 'assets/table.js').read_bytes()).hexdigest()[:12],
        'TABLE': table_head + '\n<tbody>\n' + '\n'.join(rows) + '\n</tbody>',
        'DETAILS': '\n'.join(popovers),
    }
    for key, value in replacements.items():
        template = template.replace('{{' + key + '}}', value)
    return template


def render(data):
    sources = data['sources']
    count = len(data['harnesses'])
    output = {
        'index.html': render_page(data),
        'README.md': f'# ローカルLLM ハーネス比較\n\n[**比較表を開く ↗ — 全{count}項目を1ページで比較**](https://ootsuka-repos.github.io/local-llm-harness-comparison/)\n\nローカル接続・基本コマンド・自律運用の比較表。正式コマンド、条件、エイリアス、一次資料は各セルから確認できます。\n\n確認日: {data["checked_on"]}。接続・完走は未実測。\n',
    }
    buf = io.StringIO(newline='')
    writer = csv.writer(buf, lineterminator="\n")
    writer.writerow(['harness_id','harness','feature','kind','text','official_aliases','sources','checked_on'])
    for h in data['harnesses']:
        for k,c in h['commands'].items():
            writer.writerow([h['id'],h['name'],k,c['kind'],c['text'],' ; '.join(c['aliases']),' ; '.join(sources[s]['url'] for s in c['sources']),data['checked_on']])
    output['data/commands.csv'] = buf.getvalue()
    buf = io.StringIO(newline='')
    writer = csv.writer(buf, lineterminator="\n")
    writer.writerow(['harness_id','harness','scope','local_status','protocol','connection','sources','checked_on'])
    for h in data['harnesses']:
        c = h['local']
        writer.writerow([h['id'],h['name'],h['scope'],c['status'],c['protocol'],c['text'],' ; '.join(sources[s]['url'] for s in c['sources']),data['checked_on']])
    output['data/local-models.csv'] = buf.getvalue()
    return {path: text.rstrip("\n") + "\n" for path, text in output.items()}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    data = json.loads((ROOT / 'data/harnesses.json').read_text())
    validate(data)
    outputs = render(data)
    stale = []
    for rel, text in outputs.items():
        path = ROOT / rel
        # Compare exact generated bytes.
        if args.check:
            if not path.exists() or path.read_bytes() != text.encode('utf-8'):
                stale.append(rel)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(text.encode('utf-8'))
    if stale:
        raise SystemExit('Stale generated files: ' + ', '.join(stale))
    print(f'{len(data["harnesses"])} harnesses / {len(data["harnesses"]) * len(LABELS)} capability entries / {len(data["sources"])} sources: ' + ('OK' if args.check else 'rendered'))


if __name__ == '__main__':
    main()
