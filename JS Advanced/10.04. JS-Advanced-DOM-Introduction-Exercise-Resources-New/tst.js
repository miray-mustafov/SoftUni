let jsarr = JSON.parse('["Mikes - Steve 1000, Ivan 200, Paul 800","Fleet - Maria 850, Janet 650","Mikes - Mirai 1200, Mimi 600"]')
let restaurants = {}

for(let el of jsarr){
    let [restaurant_name, workers] = el.split(' - ')
    console.log(restaurant_name +"|", workers)
    restaurants[restaurant_name] = workers
    console.log(restaurants)
    
}