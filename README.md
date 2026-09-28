# TIDES: Test-time Inference Drift Exploitation via Scaling

**Project page:** [haorandai.com/tides-paper](https://haorandai.com/tides-paper/) · **Paper:** [OpenReview](https://openreview.net/forum?id=tXRUpMp7xO) (ES-Reasoning @ ICLR 2026)

TIDES is a computation-triggered backdoor for large reasoning models. It preserves short-trace utility while degrading extended reasoning, exposing a failure mode of test-time scaling. This repository holds the source of the project page. The results shown on the page follow the extended version of the paper; the citation below is the workshop paper.

## Citation

```bibtex
@inproceedings{dai2026tides,
  title = {{TIDES}: Test-time Inference Drift Exploitation via Scaling},
  author = {Haoran Dai and Haozheng Luo and Haotian Zhang and Meng Lin and Yan Chen and Binghui Wang},
  booktitle = {The First Workshop on Efficient Spatial Reasoning},
  year = {2026},
  url = {https://openreview.net/forum?id=tXRUpMp7xO}
}
```

## Editing the page

The site is static: no build step or package installation.

- Preview with `python3 -m http.server 8000`, then open `http://localhost:8000`.
- `index.html` holds the prose, author list, tables and LaTeX; `styles.css` the layout; `script.js` math rendering and citation copying. Keep the inline citation in sync with `citation.bib`.
- `assets/results-data.json` holds the Table 1 averages and Figure 4 ablation values. `python3 scripts/render-results.py` regenerates the comparison charts and the full-results table inside their marked regions of `index.html`.
- KaTeX is self-hosted in `assets/vendor/katex`. Use `\(...\)` for inline and `\[...\]` for display math, and run `node scripts/check-math.cjs` after editing equations.

GitHub Pages serves the root of `main`.

## Credits

The paper and its figures belong to the authors. The workshop paper is shared under CC BY 4.0 on its OpenReview record; the figures and results on the page come from the extended version of the paper by the same authors. Numbers on the page are the ones reported in the paper, not an independent reproduction.
