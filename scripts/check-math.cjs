const fs = require('node:fs');
const path = require('node:path');
const katex = require('../assets/vendor/katex/katex.min.js');

const root = path.resolve(__dirname, '..');
const html = fs.readFileSync(path.join(root, 'index.html'), 'utf8');
const expressions = [...html.matchAll(/\\\[([\s\S]*?)\\\]|\\\(([\s\S]*?)\\\)/g)];
if (!expressions.length) throw new Error('No LaTeX expressions found.');

for (const match of expressions) {
  const markup = katex.renderToString(match[1] ?? match[2], {
    displayMode: match[1] !== undefined,
    output: 'htmlAndMathml',
    throwOnError: true,
    strict: 'error',
    trust: false
  });
  if (!markup.includes('<math')) throw new Error('Accessible MathML is missing.');
}

const css = fs.readFileSync(path.join(root, 'assets/vendor/katex/katex.min.css'), 'utf8');
for (const match of css.matchAll(/url\(([^)]+)\)/g)) {
  const relative = match[1].replace(/["']/g, '');
  if (!fs.existsSync(path.join(root, 'assets/vendor/katex', relative))) {
    throw new Error(`Missing math font: ${relative}`);
  }
}

console.log(`Validated ${expressions.length} LaTeX expressions and all referenced math fonts.`);
