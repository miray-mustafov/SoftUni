function extractText() {
    const list = Array.from(document.querySelectorAll('li'))
    const result = list.map(e => e.textContent).join('\n')

    document.getElementById('result').value = result
}