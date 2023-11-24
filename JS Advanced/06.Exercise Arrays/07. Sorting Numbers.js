function smallest_biggest(arr){
    let res = []

    arr.sort((a,b) => a-b)
    //console.log(arr)
    let etrem = arr.length/2
    for (let _ = 0; _ < etrem; _++) {
        res.push(arr.shift())
        res.push(arr.pop())
    }

    
    if(arr.length % 2 !== 0){
        res.pop()
    }
    
    //console.log(res)
    return res
}

smallest_biggest([1, 65, 3, 52, 48, 63, 31, -3, 18,56])