function sumTable() {

    const arr = Array.from(document.querySelectorAll('tr')).slice(1,-1);
    const last_tr = Array.from(document.querySelectorAll('tr'))[arr.length+1].lastElementChild;
    let sum = 0
    arr.forEach(e => sum += + e.lastElementChild.textContent)
    last_tr.textContent = sum
}