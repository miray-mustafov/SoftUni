function addItem() {
    function onDelete(event){
        event.target.parentElement.remove()
    }

    const input = document.getElementById('newItemText')
    const new_li = document.createElement('li')
    new_li.textContent = input.value   
    document.getElementById('items').appendChild(new_li)

    const btnDel = document.createElement('a')
    btnDel.textContent = '[Delete]'
    btnDel.href='#'
    btnDel.addEventListener('click',onDelete)
    new_li.appendChild(btnDel)
    
    input.value = ''
}
