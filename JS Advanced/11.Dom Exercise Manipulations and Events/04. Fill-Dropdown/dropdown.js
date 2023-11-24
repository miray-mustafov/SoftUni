function addItem() {
    const txt_field = document.getElementById('newItemText')
    const value_field = document.getElementById('newItemValue')
    const menu = document.getElementById('menu')

    let new_option = document.createElement('option')
    new_option.textContent = txt_field.value
    new_option.value = value_field.value

    menu.appendChild(new_option)

    txt_field.value = ''
    value_field.value = ''
}