function solve() {
    const input = {
        task: document.getElementById('task'),
        descr: document.getElementById('description'),
        date: document.getElementById('date')
    }
    let [_, openSec, inProgSec, complSec] = document.querySelectorAll('section div:nth-child(2)')
    console.log()
    document.getElementById('add').addEventListener('click', onAdd)

    function onAdd(event) {
        event.preventDefault(); // STOP PAGE REFRESHING
        
        if(Object.values(input).some((el) => el.value == '')){
            return
        }

        let article = document.createElement('article')
        let h3 = create_el('h3', input.task.value)
        let p1 = create_el('p', 'Description: ' + input.descr.value)
        let p2 = create_el('p', 'Due Date: ' + input.date.value)
        let div = create_el('div', '', 'flex')
        let btn_start = create_el('button', 'Start', 'green')
        btn_start.addEventListener('click', onStart)
        let btn_delete = create_el('button', 'Delete', 'red')
        btn_delete.addEventListener('click', onDelete)
        let btn_finish = create_el('button', 'Finish', 'orange')
        btn_finish.addEventListener('click', onFinish)
        

        article.appendChild(h3)
        article.appendChild(p1)
        article.appendChild(p2)
        div.appendChild(btn_start)
        div.appendChild(btn_delete)
        
        article.appendChild(div)

        openSec.appendChild(article)
        Object.values(input).forEach(i => i.value = '')

        function onStart() {
            btn_start.remove()
            div.appendChild(btn_finish)
            inProgSec.appendChild(article)
        }
        function onDelete() {
            article.remove(article)
        }
        function onFinish() {
            div.remove()
            complSec.appendChild(article)
        }
    }
    
    function create_el(type, txt_cont, class_) {
        let element = document.createElement(type)
        if (txt_cont) { element.textContent = txt_cont }
        if (class_) { element.className = class_ }
        return element
    }
}