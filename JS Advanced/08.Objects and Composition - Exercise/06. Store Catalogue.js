function store_catalogue(goods){
    let result = {
        A: [],
        B: [],
        C: [],
        D: [],
        E: [],
        F: [],
        G: [],
        H: [],
        I: [],
        J: [],
        K: [],
        L: [],
        M: [],
        N: [],
        O: [],
        P: [],
        Q: [],
        R: [],
        S: [],
        T: [],
        U: [],
        V: [],
        W: [],
        X: [],
        Y: [],
        Z: []
    }

    for (let i = 0; i < goods.length; i++) {
        let current_f_letter = goods[i][0]  //will be always upper case
        let [name, price] = goods[i].split(' : ')

        result[current_f_letter].push({name, price})
    }

    let result_list = Object.entries(result)
    let sorted_arr = []
    for(let [lett, arr] of result_list){
        
        if(arr == false){continue}

        sorted_arr.push(lett , // lett is indx 0 and next the arr
            arr.sort(function (a,b){
            return a.name.localeCompare(b.name)
        })
        )
    }

    for (let i = 0; i < sorted_arr.length; i+=2) {
        let lett = sorted_arr[i]
        let arr = sorted_arr[i+1]

        console.log(lett)
        arr.forEach(element => { 
            console.log(`  ${element.name}: ${element.price}`) });
    }
}

store_catalogue(
    ['Appricot : 20.4',
    'Fridge : 1500',
    'TV : 1499',
    'Deodorant : 10',
    'Boiler : 300',
    'Apple : 1.25',
    'Anti-Bug Spray : 15',
    'T-Shirt : 10']
)

store_catalogue(
    ['Banana : 2',
    'Rubic\'s Cube : 5',
    'Raspberry P : 4999',
    'Rolex : 100000',
    'Rollon : 10',
    'Rali Car : 2000000',
    'Pesho : 0.000001',
    'Barrel : 10']
)