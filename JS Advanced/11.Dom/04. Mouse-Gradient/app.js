function attachGradientEvents() {
    let gradient_ref = document.getElementById('gradient')
    let result_ref = document.getElementById('result')
    
    gradient_ref.addEventListener('mousemove', onMouseMove)
    gradient_ref.addEventListener('mouseleave',onMouseLeave)

    function onMouseLeave(ev){
        result_ref.textContent = ''
    }

    function onMouseMove(ev){

        let percentage = Math.floor(ev.offsetX/gradient_ref.clientWidth*100)
        result_ref.textContent = percentage+'%' 

    }
}