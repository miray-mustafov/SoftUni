function create(words) {
   const parent_div = document.getElementById('content')

   for (let word of words) {
      let new_div = document.createElement('div')
      let new_par = document.createElement('p')
      new_par.textContent = word
      new_par.style.display = 'none'

      new_div.addEventListener('click', onClick)
      new_div.appendChild(new_par)
      parent_div.appendChild(new_div)
   }

   function onClick(ev){
      ev.currentTarget.querySelector('p').style.display = ''

   }
}  