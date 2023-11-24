window.addEventListener("load", solve);

function solve() {
    let type_product = document.getElementById('type-product')
    let inp = {
        description: document.getElementById('description'),
        client_name: document.getElementById('client-name'),
        client_phone: document.getElementById('client-phone')
    }
    let orders = {
        received: document.getElementById('received-orders'),
        completed: document.getElementById('completed-orders')
    }
    //document.getElementById('type-product').children[0].selected

    let sendBtn = document.querySelector('button[type=submit]')
    sendBtn.addEventListener('click', onSend)
    document.querySelector('button.clear-btn').addEventListener('click', ()=>{
        let completed_divs = orders.completed.querySelectorAll('div')
        completed_divs.forEach(element => {
            element.remove();
        });
    })

    function onSend(ev) {
        ev.preventDefault()
        let desc = inp.description.value
        let name = inp.client_name.value
        let phone = inp.client_phone.value

        if (desc == '' || name == '' || phone == '') {
            return;
        }

            let div = document.createElement('div')
            div.className = 'container'
            div.innerHTML = `
                <h2>Product type for repair: ${type_product.value}</h2>
                <h3>Client information: ${name}, ${phone}</h3>
                <h4>Description of the problem: ${desc}</h4>
                <button class="start-btn">Start repair</button>
                <button class="finish-btn" disabled>Finish repair</button>`
            let startRepBtn = div.querySelector('button.start-btn')
            let finishRepBtn = div.querySelector('button.finish-btn')
            startRepBtn.addEventListener('click', onStartRepair)
            finishRepBtn.addEventListener('click', onFinishRepair)

        orders.received.appendChild(div)
        Object.keys(inp).forEach(field => inp[field].value = '');

        function onStartRepair() {
            finishRepBtn.disabled = ''
            startRepBtn.disabled = 'none'
        } 
        function onFinishRepair(){
            startRepBtn.remove()
            finishRepBtn.remove()
            orders.completed.appendChild(div)
        }
    }
}