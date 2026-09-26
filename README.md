# TIDES project website

**TIDES: Test-time Inference Drift Exploitation via Scaling**

- Paper record: https://openreview.net/forum?id=tXRUpMp7xO
- Displayed status: ICLR 2026 · ES-Reasoning Workshop
- Public website: https://haorandai.com/tides-paper/
- Website repository: https://github.com/haorandai/tides-paper

## Preview and edit

Run `python3 -m http.server 8000` in this directory, then open `http://localhost:8000`.

Edit `index.html` for prose, author metadata, tables and LaTeX; `styles.css` for layout; and `script.js` for math rendering and citation copying. Keep the inline citation synchronized with `citation.bib`.

KaTeX 0.18.9, fonts and license are self-hosted in `assets/vendor/katex`. Use inline `\(...\)` and display `\[...\]` math. Run `node scripts/check-math.cjs` after equation edits. The site has no build step or package installation.

## Evidence and attribution

Content follows the exact PDF linked from the supplied OpenReview record. Numerical comparisons are manuscript-reported results, not an independent reproduction. Figure crops preserve the original panels and labels. Citation for the ES-Reasoning workshop paper.

Authors and status were verified against the record on September 26, 2026. Haoran Dai and Haozheng Luo are equal contributors, confirmed in the PDF and by the user.

The underlying paper and figures belong to their authors. The OpenReview record specifies CC BY 4.0. Page design adapts the authors' OASIS project page. Geist is loaded from Google Fonts with system fallbacks. No source manuscript, private reviews, research checkpoints, or private repository contents are included.

## Hosting

GitHub Pages serves the root of `main`; `.nojekyll` enables direct static-file serving. Asset paths are relative. This website repository is independent of the research-code repository and the personal homepage. Verify deployment status and the public URL after pushing updates.
