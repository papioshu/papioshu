# Maintaining this profile

This repo (`papioshu/papioshu`) is the GitHub profile README. Whatever `README.md` holds on `main` shows on https://github.com/papioshu.

## Updating projects
- **Selected Work** table: one row per featured project. Link only public repos; private ones say "Private" with no link.
- **Projects** `<details>` block: the full directory, grouped by category. Keep the blank line after `<summary>` and before `</details>`, or GitHub won't render the Markdown inside.
- Open every live link and confirm it loads before adding it. Never name unreleased products or private architecture.
## Artwork
- `assets/paperhand-original.png` is Rich's original crane / PH logo. **Never edit, redraw, or regenerate it.** To replace it, overwrite it with a new original supplied by Rich.
- `paperhand-mark.png` and `paperhand-header.png` are built from the original by `scripts/build_assets.py`, which only scales and composites it. Brand purple is `#8F63EC`, sampled from the original.
- Rebuild after changing the original or the header text: `pip install Pillow`, then `python scripts/build_assets.py` from the repo root. It uses the Windows system fonts Bahnschrift and Segoe UI.
