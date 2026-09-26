# TIDES project website

**TIDES: Test-time Inference Drift Exploitation via Scaling**

- Paper record: https://openreview.net/forum?id=tXRUpMp7xO
- Displayed status: Extended version (content from the extended paper; page does not name the venue under review)
- Public website: https://haorandai.com/tides-paper/
- Website repository: https://github.com/haorandai/tides-paper

## Preview and edit

Run `python3 -m http.server 8000` in this directory, then open `http://localhost:8000`.

Edit `index.html` for prose, author metadata, tables and LaTeX; `styles.css` for layout; and `script.js` for math rendering and citation copying. Keep the inline citation synchronized with `citation.bib`.

`assets/results-data.json` contains the source-reported Table 1 averages and Figure 4 ablation values. Run `python3 scripts/render-results.py` to update the static comparison charts and the expandable full-results table. The generator only updates its marked regions in `index.html`; surrounding prose stays editable. It preserves missing Base RAS values and uses a fixed 0-100 chart scale. The original figure assets remain available through full-size links.

KaTeX 0.18.9, fonts and license are self-hosted in `assets/vendor/katex`. Use inline `\(...\)` and display `\[...\]` math. Run `node scripts/check-math.cjs` after equation edits. The site has no build step or package installation.

## Evidence and attribution

Prose, figures, and results follow the extended version of the paper (three models: Phi-4-Reasoning, DeepSeek-R1-Distill-Qwen-7B, and -Llama-8B; five benchmarks). Numerical comparisons are manuscript-reported results, not an independent reproduction. Figure crops preserve the original panels and labels. The BibTeX citation is for the earlier ES-Reasoning workshop paper, which is the public, citeable version; the page notes this. Extended-version source figures and the parsed Table 1 are kept locally in `website-pipeline/sources/tides-iclr27/`, outside this repository.

The displayed author list is the extended-version team of eight, confirmed by the user on September 26, 2026. "Meng Lin" is capitalized at the user's request, including in the BibTeX. Haoran Dai and Haozheng Luo are equal contributors. The BibTeX author list is the six-author workshop record and is intentionally left unchanged.

The underlying paper and figures belong to their authors. The OpenReview record specifies CC BY 4.0. Page design adapts the authors' OASIS project page. Geist is loaded from Google Fonts with system fallbacks. No source manuscript, private reviews, research checkpoints, or private repository contents are included.

## Hosting

GitHub Pages serves the root of `main`; `.nojekyll` enables direct static-file serving. Asset paths are relative. This website repository is independent of the research-code repository and the personal homepage. Verify deployment status and the public URL after pushing updates.
