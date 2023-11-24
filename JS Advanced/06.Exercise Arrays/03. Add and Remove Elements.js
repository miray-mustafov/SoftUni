function add_remove(commands){
    function add_comm(result, i){
        result.push(i)
        return ++i
    }
    function remove_comm(result,i){
        result.pop()
        return ++i
    }

    let result = []
    let i = 1
    for(let comm of commands){
        (comm === 'add' ? i = add_comm(result, i) : i = remove_comm(result,i))
    }
    
    console.log(result.length == '0' ? 'Empty' : result.join('\n'))
}

add_remove(['remove', 'remove'])