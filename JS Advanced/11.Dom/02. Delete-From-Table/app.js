function deleteByEmail() {
    const input_field = document.querySelector('input[name="email"]')
    const input_value = input_field.value
    const  emails = [...document.querySelectorAll("tbody tr")]
    
    let found = false
    for(let email of emails){

        if(input_value === email.children[1].textContent){
            found = true
            email.remove()
        }
    }

    input_field.value = ''
    document.getElementById('result').textContent = found ? "Deleted." : "Not found." 

}