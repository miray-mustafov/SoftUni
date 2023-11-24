function assemble_car(chars_car){
    // things u have in ur car FACTORY
    const engines = [{ power: 90, volume: 1800 }, {power: 120, volume: 2400} ,{power: 200, volume: 3500 }]
    const carriages = [{type: "hatchback", color: chars_car.color} , {type: "coupe", color: chars_car.color}]
    
    // now we filter the engine with closest up hpower
    let suitable_engine;
    for (let i = 0; i < engines.length; i++) {
        if(engines[i].power >= chars_car.power){
            suitable_engine = engines[i]
            break
        }
    }

    let col = chars_car.wheelsize % 2 === 0 ? chars_car.wheelsize - 1 : chars_car.wheelsize
    let a = 5
    return {
        model: chars_car.model,
        engine: suitable_engine,
        carriage: carriages.filter(c => c.type === chars_car.carriage).shift(),
        wheels: [col,col,col,col]
        
    }

}

console.log(assemble_car({ 
    model: 'VW Golf II',
    power: 90,
    color: 'blue',
    carriage: 'hatchback',
    wheelsize: 14 }
))
console.log('----')

console.log(assemble_car({ 
    model: 'Opel Vectra',
    power: 110,
    color: 'grey',
    carriage: 'coupe',
    wheelsize: 17 }
))
