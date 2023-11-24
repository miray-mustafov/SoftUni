function solve() {
  function transform(i) {
    for (; i < words.length; i++) {

      if (words[i] == false) { continue }
      result += words[i][0].toUpperCase() + words[i].slice(1).toLowerCase()
    }
  }
     
  const text = document.getElementById('text').value
  const convention = document.getElementById('naming-convention').value
  const result_place = document.getElementById('result')

  let words = text.split(' ')
  let result = ''

  if (convention === "Camel Case") {
    transform(1)
    result = words.shift().toLowerCase() + result
  }
  else if (convention === "Pascal Case") {
    transform(0)
  }
  else {
    result = 'Error!'
  }

  result_place.textContent = result
}