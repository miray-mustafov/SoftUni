function lowest_price(data){
    let result = []
    let prod_names = []

    for (let i = 0; i < data.length; i++) {
        let [town, product, price] = data[i].split(' | ')
        price = Number(price)

        if(prod_names.filter(pr => pr === product)== false){
            result.push({product,price,town})
            prod_names.push(product)
            continue
        }

        for (let j = 0; j < result.length; j++) {
            if(result[j].product === product && price < result[j].price ){
                result[j].price = price
                result[j].town = town
            }    
        }
    }

    for (let i = 0; i < result.length; i++) {
        console.log(`${result[i].product} -> ${result[i].price} (${result[i].town})`)
    }
}

lowest_price(['Sample Town | Sample Product | 1000',
'Sample Town | Orange | 2',
'Sample Town | Peach | 1',
'Sofia | Orange | 3',
'Sofia | Peach | 2',
'New York | Sample Product | 1000.1',
'New York | Burger | 10']

)