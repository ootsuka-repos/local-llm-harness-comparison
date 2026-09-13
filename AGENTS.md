# Maintenance

- Japanese documentation; preserve exact upstream command spellings.
- `data/harnesses.json` is the source of truth. Generate tables with `python3 scripts/render.py`.
- The public site is a single comparison table showing all 17 rows. Do not add recommendation sections, cards, pagination, or separate detail pages.
- Edit `site/template.html` and `assets/` for presentation. `index.html`, `README.md`, and the CSV files are generated; do not edit them directly.
- Cell summaries are reviewed display labels. Keep full syntax, aliases, conditions, and primary sources in the same catalog entry and its accessible popover.
- Cite primary documentation for each capability. Distinguish CLI, slash command, environment/config, SDK, extension, and unverified behavior.
- Never turn "not verified" into "unsupported" without evidence.
- Local inference compatibility is not an end-to-end benchmark or proof of offline operation.
- Keep current, preview, and legacy surfaces separate. Record the research date and repository revisions.
- Do not install harnesses, execute example agent commands, or change the user's model settings when maintaining this comparison.
- Check with `python3 scripts/render.py --check` before committing.
