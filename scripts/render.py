#!/usr/bin/env python3
"""Validate the catalog and render Markdown / CSV without third-party dependencies."""
import argparse
import csv
import io
import json
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


def esc(value):
    return str(value).replace("|", "&#124;").replace("\n", "<br>")


def table(headers, rows):
    return "\n".join(["| " + " | ".join(map(esc, headers)) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"] + ["| " + " | ".join(map(esc, r)) + " |" for r in rows]) + "\n"


def validate(data):
    sources = data["sources"]
    ids = [h["id"] for h in data["harnesses"]]
    assert len(ids) == len(set(ids)), "duplicate harness id"
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
        assert h["notes"] and h["scope"]


def render(data):
    sources = data["sources"]
    def refs(keys):
        return " ".join(f'[{k}]({sources[k]["url"]})' for k in keys)
    def cell(c):
        return c["text"] + " " + refs(c["sources"])
    intro = f'確認日: **{data["checked_on"]}**。公式ドキュメント／上流ソースに基づく比較。LLM接続・完走は未実測。\n\n'
    intro += '[読み方と対象範囲](../README.md) · [ローカル接続](local-models.md) · [コマンド](commands.md) · [放置運用](autonomy.md) · [個別詳細](details.md) · [出典](sources.md)\n\n'
    output = {}
    rows = []
    local_names = {"supported": "対応経路あり", "conditional": "条件付き", "unverified": "公式経路未確認"}
    for h in data["harnesses"]:
        rows.append([h["name"], h["scope"], local_names[h["local"]["status"]], h["local"]["protocol"], cell(h["local"])])
    output["docs/local-models.md"] = '# ローカルLLM対応比較\n\n' + intro + table(['ハーネス', '対象・世代', 'ローカル推論', 'API形式', '接続方法・制約'], rows)
    groups = [
        ("commands", "機能別コマンド対応表", [["start", "model", "headless", "resume"], ["plan", "compact", "approval", "output"]]),
        ("autonomy", "放置運用の機能比較", [["goal", "test", "limits"], ["delegate", "schedule", "sandbox", "extend"]]),
    ]
    for filename, title, sections in groups:
        out = f'# {title}\n\n' + intro
        out += '表中のコマンドは同じ目的に対する対応関係です。CLI間で完全に同じ挙動になるエイリアスではありません。`PROMPT` / `MODEL` / `ID` は置換用です。\n\n'
        for keys in sections:
            out += table(["ハーネス", *[LABELS[k] for k in keys]], [[h["name"], *[cell(h["commands"][k]) for k in keys]] for h in data["harnesses"]]) + '\n'
        output[f'docs/{filename}.md'] = out
    out = '# 個別仕様・正式エイリアス\n\n' + intro
    for h in data["harnesses"]:
        out += f'## {h["name"]}\n\n対象: {h["scope"]}\n\n公式: [{h["upstream"]}]({h["upstream"]})\n\n'
        out += cell(h["local"]) + '\n\n'
        out += table(['機能', '操作種別', '正式コマンド／機能', '公式の短縮形・別名'], [[LABELS[k], c['kind'], cell(c), '<br>'.join(c['aliases']) or '—'] for k,c in h['commands'].items()])
        out += '\n' + '\n'.join('- ' + n for n in h['notes']) + '\n\n'
    output['docs/details.md'] = out
    output['docs/sources.md'] = '# 出典台帳\n\n' + intro + 'GitHubの出典は可能な限り確認時のコミットへ固定しています。Webドキュメントは随時更新されます。取得記録は [source-audit.json](../data/source-audit.json)、リポジトリの参照点は [upstream-revisions.json](../data/upstream-revisions.json) にあります。\n\n' + table(['ID', '一次資料', '確認日'], [[k,f'[{s["title"]}]({s["url"]})',s['checked_on']] for k,s in sources.items()])
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
            path.write_bytes(text.encode('utf-8'))
    if stale:
        raise SystemExit('Stale generated files: ' + ', '.join(stale))
    print(f'{len(data["harnesses"])} harnesses / {len(data["harnesses"]) * len(LABELS)} capability entries / {len(data["sources"])} sources: ' + ('OK' if args.check else 'rendered'))


if __name__ == '__main__':
    main()
