function towns_to_json(data){
    let result = []

    class Town{
        constructor(town, latitude, longitude){
            this.Town = town
            this.Latitude = latitude // num
            this.Longitude= longitude // num
        }
    }

    data.shift()
    for(let town of data){
        let [name, latitude, longitude] = town.slice(2,-2).split(' | ')
        latitude = + Number(latitude).toFixed(2)
        longitude = + Number(longitude).toFixed(2)
        
        let new_town = new Town(name, latitude, longitude)
        result.push(new_town)
    }
    return (JSON.stringify(result))
    //console.log(JSON.stringify(result))
}

console.log(towns_to_json(
    ['| Town | Latitude | Longitude |',
    '| Sofia | 42.696552 | 23.32601 |',
    '| Beijing | 39.913818 | 116.363625 |']
    ))