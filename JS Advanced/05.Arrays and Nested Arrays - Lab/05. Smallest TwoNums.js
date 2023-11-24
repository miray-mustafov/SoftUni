function twoSmallest(nums){
    if(nums.length === 1){
        console.log(nums[0])
        return
    }
    let smallest_two = []

    let current_smallest=Math.min(...nums)
    smallest_two.push(current_smallest)
    for (let i = 0; i < nums.length; i++) {

        if (current_smallest === nums[i])
            nums.splice(i,1)
        
    }


    current_smallest=Math.min(...nums)
    smallest_two.push(current_smallest)
     
    console.log(...smallest_two) 
} 

twoSmallest([4]);