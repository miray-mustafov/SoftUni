function calorie(listt){
    const obj = {}
    for (let i = 0; i < listt.length; i+=2) {
        const key = listt[i]
        const value = Number(listt[i+1])

        obj[key] = value
    }
    console.log(obj)
}

calorie(['Yoghurt', '48', 'Rise', '138', 'Apple', '52'])
calorie(['Potato', '93', 'Skyr', '63', 'Cucumber', '18', 'Milk', '42'])
