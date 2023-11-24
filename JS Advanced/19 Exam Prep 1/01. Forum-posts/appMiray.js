window.addEventListener("load", solve);

function solve() {
    const input = {
        title: document.getElementById('post-title'),
        categ: document.getElementById('post-category'),
        content: document.getElementById('post-content'),
    }
    const lists = {
        reviw: document.getElementById("review-list"),
        published: document.getElementById("published-list"),
    }

    let publishBTN = document.getElementById('publish-btn')
    let clearBTN = document.getElementById('clear-btn')
    publishBTN.addEventListener('click', onPublish)
    clearBTN.addEventListener('click', onClear)

    function onPublish(ev) {
        ev.preventDefault()
        if(input.title.value=='' || input.categ.value=='' ||input.content.value==''){
            return;
        }
        let titl = input.title.value
        let catg = input.categ.value
        let cont= input.content.value
        
        let li = document.createElement('li')
        li.classList.add('rpost')
        li.innerHTML = `
        <article>
            <h4>${titl}</h4>
            <p>Category: ${catg}</p>
            <p>Content: ${cont}</p>
        </article>
        <button class="action-btn edit">Edit</button>
        <button class="action-btn approve">Approve</button>`
        li.querySelector('.edit').addEventListener('click', onEdit)
        li.querySelector('.approve').addEventListener('click', onApprove)

        lists.reviw.appendChild(li)

        input.title.value = ''
        input.categ.value = '' 
        input.content.value = '' 

        function onEdit(){
            input.title.value = titl 
            input.categ.value = catg 
            input.content.value = cont 
            li.remove()
        }
        function onApprove(){
            li.querySelector('.edit').remove()
            li.querySelector('.approve').remove()
            lists.published.appendChild(li)
        }
    }
    function onClear(){
        lists.published.innerHTML = ''
    }
}