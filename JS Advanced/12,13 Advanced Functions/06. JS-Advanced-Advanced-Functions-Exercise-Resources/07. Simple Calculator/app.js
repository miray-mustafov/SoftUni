function calculator() {
    let num1, num2, result;

    return {
        init,
        add,
        subtract
    }

    function add() {
        result.value = +num1.value + +num2.value
    }
    function subtract() {
        result.value = +num1.value - +num2.value
    }
    function init(n1, n2, r) {
        num1 = document.getElementById(n1)
        num2 = document.getElementById(n2)
        result = document.getElementById(r)
    }
}