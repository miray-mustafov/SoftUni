function neGPos(nums){
    let result = []
    for (let num of nums){
        if(num<0){
            result.unshift(num)
            continue
        }
        result.push(num)

    }
    console.log(...result)
}

neGPos([7, -2, 8, 9])
console.log('sokem aazana we')
neGPos([3, -2, 0, -1])