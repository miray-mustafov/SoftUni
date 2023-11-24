function is_magical(arr){
    let magical = true;
    for (let i = 0; i < arr.length-1; i++) {
        let sum_row_a = arr[i].reduce((a,b) => a + b ,0)
        let sum_row_b = arr[i+1].reduce((a,b) => a + b ,0)

        if(sum_row_a !== sum_row_b)
        {
            //console.log(false)
            return false 
        }
    }
    //console.log(true)
    return true
    
}

is_magical([[4, 5, 6],
    [6, 5, 4],
    [5, 5, 5]]
   )


   is_magical([[11, 32, 45],
    [21, 0, 1],
    [21, 1, 1]]
   
   )