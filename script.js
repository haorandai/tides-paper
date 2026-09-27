const copyButton = document.querySelector('#copy-citation');
const status = document.querySelector('#copy-status');
copyButton?.addEventListener('click', async () => {
  const text = document.querySelector('#bibtex').textContent;
  try {
    await navigator.clipboard.writeText(text);
    copyButton.textContent = 'Copied';
    status.textContent = 'BibTeX copied to clipboard.';
    setTimeout(() => { copyButton.textContent = 'Copy BibTeX'; }, 2400);
  } catch {
    const selection = window.getSelection();
    const range = document.createRange();
    range.selectNodeContents(document.querySelector('#bibtex'));
    selection.removeAllRanges();
    selection.addRange(range);
    status.textContent = 'Citation selected. Press Ctrl+C or ⌘C to copy, or download the .bib file.';
  }
});

try {
  renderMathInElement(document.querySelector('main'), {
    delimiters: [
      { left: '\\[', right: '\\]', display: true },
      { left: '\\(', right: '\\)', display: false }
    ],
    output: 'htmlAndMathml',
    throwOnError: true,
    strict: 'error',
    trust: false
  });
} catch (error) {
  console.error('Math rendering failed.', error);
}
