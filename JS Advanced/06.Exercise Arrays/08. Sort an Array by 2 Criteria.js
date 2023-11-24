function sokem(arr){
    arr.sort(sort_function)

    function sort_function(a,b){
        if(a.length === b.length){
            return a.localeCompare(b)
        }

        return a.length - b.length
    }
    console.log(arr.join(`\n`))
}

sokem(['Isacc', 
'Theodor', 
'Jack', 
'Harrison', 
'George']
)