function towns(listt){
    const result = {}

    for(let town of listt){
        let [town_name, town_population] = town.split(' <-> ')
        town_population = Number(town_population)

        if (result[town_name] === undefined){
            result[town_name] = town_population
        }
        else{
            result[town_name] += town_population;
        }
    }

    for(let[town_name, town_population] of Object.entries(result)){
        console.log(`${town_name} : ${town_population}`)
    }

}

towns(['Istanbul <-> 100000',
'Honk Kong <-> 2100004',
'Jerusalem <-> 2352344',
'Mexico City <-> 23401925',
'Istanbul <-> 1000']
)