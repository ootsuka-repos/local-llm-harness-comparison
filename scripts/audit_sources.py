#!/usr/bin/env python3
"""Read-only HTTP audit of primary source URLs; no model calls or installers."""
import concurrent.futures
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parents[1]


def fetch(item):
    sid, source = item
    url = source['url']
    # Fetch immutable GitHub source directly rather than rendered navigation HTML.
    fetch_url = url.replace('https://github.com/', 'https://raw.githubusercontent.com/', 1).replace('/blob/', '/', 1) if '/blob/' in url and url.startswith('https://github.com/') else url
    row = {'source_id': sid, 'url': url, 'fetch_url': fetch_url}
    try:
        req = urllib.request.Request(fetch_url, headers={'User-Agent': 'local-llm-harness-comparison/1.0'})
        with urllib.request.urlopen(req, timeout=25) as response:
            body = response.read()
            row.update(status=response.status, final_url=response.url, bytes=len(body), sha256=hashlib.sha256(body).hexdigest())
    except Exception as exc:
        row.update(status='error', error=str(exc))
    return row


def main():
    catalog = json.loads((ROOT / 'data/harnesses.json').read_text())
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        rows = list(pool.map(fetch, catalog['sources'].items()))
    result = {'audited_at_utc': datetime.now(timezone.utc).isoformat(), 'note': 'HTTP/content audit only; not semantic verification or end-to-end model testing.', 'sources': rows}
    (ROOT / 'data/source-audit.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    errors = [r for r in rows if r['status'] != 200]
    for row in errors:
        print(row['source_id'], row.get('error', row['status']))
    print(f'{len(rows) - len(errors)}/{len(rows)} sources fetched successfully')
    if errors:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
