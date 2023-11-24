function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick);
   
   
   const searched = document.getElementById('searchField') // .value
   const info_htmlcoll = document.getElementsByTagName('tbody')[0].children

   function onClick() {
      
      for(let tr of info_htmlcoll){
         tr.classList.remove('select')

         if(tr.innerHTML.includes(searched.value)){
            tr.className = 'select'
         }
      }
      searched.value = ''
   }
}