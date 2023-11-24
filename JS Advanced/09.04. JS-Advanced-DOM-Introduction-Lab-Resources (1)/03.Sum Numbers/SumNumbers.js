function calc() {
    const n1 = Number(document.getElementById('num1').value) 
    const n2 = Number(document.getElementById('num2').value) 
    const sum_n1_n2 = n1+n2
    
    if(Number.isNaN(sum_n1_n2)){
        alert('sokem aazana')
    }
    else{
        document.getElementById('sum').value = sum_n1_n2 
    }
}
