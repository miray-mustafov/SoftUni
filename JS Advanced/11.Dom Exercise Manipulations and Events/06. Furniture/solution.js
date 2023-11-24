function solve() {
  let [generateBtn, buyBtn] = [...document.querySelectorAll('button')]
  generateBtn.addEventListener('click', onGenerate)
  buyBtn.addEventListener('click', onBuy)

  function onGenerate(ev){
    let input = document.querySelector('textarea')
    console.log(JSON.parse(input.value))
  }

  function onBuy(ev){
    
    
  }
}