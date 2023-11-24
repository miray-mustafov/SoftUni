function sumFL(listt){
    const first = [...listt].shift()
    const last = listt.pop()
    let sum = Number(first) + Number(last)
    console.log(sum)
}

sumFL(['20', '30', '40'])
sumFL(["10"])
sumFL(['5', '10'])
