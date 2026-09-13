# Maintenance

- Japanese documentation; preserve exact upstream command spellings.
- `data/harnesses.json` is the source of truth. Generate tables with `python3 scripts/render.py`.
- The public site is a single comparison table showing all 17 rows. Do not add recommendation sections, cards, pagination, or separate detail pages.
- Edit `site/template.html` and `assets/` for presentation. `index.html`, `README.md`, and the CSV files are generated; do not edit them directly.
- Command cell summaries must display literal upstream commands, flags, API symbols, or config keys in backticks, never Japanese paraphrases. If no verified invocation exists, use an explicit operation marker (e.g. MODEL, CONFIG, EXTENSION, UNVERIFIED). Keep full syntax, aliases, conditions, and primary sources in the same catalog entry and its accessible popover.
- Allow horizontal scrolling for long literal commands while keeping all 17 rows compact and the product-name column fixed. Never truncate or arbitrarily wrap command names to force all columns into one viewport.
- Cite primary documentation for each capability. Distinguish CLI, slash command, environment/config, SDK, extension, and unverified behavior.
- Never turn "not verified" into "unsupported" without evidence.
- Local inference compatibility is not an end-to-end benchmark or proof of offline operation.
- Keep current, preview, and legacy surfaces separate. Record the research date and repository revisions.
- Do not install harnesses, execute example agent commands, or change the user's model settings when maintaining this comparison.
- Check with `python3 scripts/render.py --check` before committing.
