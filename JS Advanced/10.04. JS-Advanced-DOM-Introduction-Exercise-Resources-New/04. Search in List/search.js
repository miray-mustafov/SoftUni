function search() {
   let towns_str = document.getElementsByTagName('ul')[0].children
   let substr = document.getElementById('searchText').value
   let counter = 0;
   let resul = document.getElementById('result')


   for(let el of towns_str){
      el.style.fontWeight = 'normal'
      el.style.textDecoration='none'

      let curr_town_str = el.textContent

      if (curr_town_str.match(substr)){
         counter++;
         el.style.fontWeight = 'bold'
         el.style.textDecoration='underline'
      }
   }
   resul.textContent = 'Malko momichence';
}
