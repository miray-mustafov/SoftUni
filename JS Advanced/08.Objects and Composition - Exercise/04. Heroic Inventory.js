function make_heroes(input){
    let result = []

    for (let i = 0; i < input.length; i++) {
        let [name, level, items] = input[i].split(' / ')   
        level = Number(level)
        items = items.split(', ')
        
        result.push({name,level,items}) 
        // =={name: name..} qvno jsa e mn umen i izkarva
        // imeto na promelivata kat kluch a 
        // stoinosta q slaga kyt value na obekta
        let a = 5
    }
    console.log(JSON.stringify(result))
}

make_heroes(
['Isacc / 25 / Apple, GravityGun',
'Derek / 12 / BarrelVest, DestructionSword',
'Hes / 1 / Desolator, Sentinel, Antara']
)