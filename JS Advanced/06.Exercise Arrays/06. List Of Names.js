function orderAlpha(names){
    names.sort((a,b) => a.localeCompare(b))

    for (let i = 0; i < names.length; i++) {
        console.log(`${i+1}.${names[i]}`)        
    }
}

orderAlpha(["John", "Bob", "Christina", "Ema"])