function validate() {
    let email = document.getElementById('email')
    const re = new RegExp('\\b[a-z]([a-z]+)?@[a-z]+\\.[a-z]+\\b')
    
    email.addEventListener('change', onChange)
    
    function onChange(event){
        let is_valid = re.test(this.value)
        console.log(is_valid)
        if(!is_valid){
            email.classList.remove('valid')
            email.classList.add('error')
        }
        else{
            email.classList.remove('error')
            email.classList.add('valid')
        }

    }
    


}