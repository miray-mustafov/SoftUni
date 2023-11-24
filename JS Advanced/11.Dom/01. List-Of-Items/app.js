function addItem() {
    const input = document.getElementById('newItemText')
    const new_li = document.createElement('li')
    new_li.textContent = input.value   
    document.getElementById('items').appendChild(new_li)
    input.value = ''
}