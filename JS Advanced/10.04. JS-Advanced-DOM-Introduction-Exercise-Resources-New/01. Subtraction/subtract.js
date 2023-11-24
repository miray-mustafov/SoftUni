function subtract() {
    const n1 = + document.getElementById('firstNumber').value
    const n2 = + document.getElementById('secondNumber').value
    const result = n1 - n2
    const ref_to_place = document.querySelector('div div')
    ref_to_place.textContent = result
    
}