function f(arr){
    let new_arr = [arr[0]]
    let counter = 0;
    for (let i = 0; i < arr.length-1; i++) {

        if(new_arr[i - counter] < arr[i + 1]){
            new_arr.push(arr[i + 1])      
        }
        else{
            counter++
        }
        
    }

    //return new_arr
    console.log(new_arr)
}

f([20])