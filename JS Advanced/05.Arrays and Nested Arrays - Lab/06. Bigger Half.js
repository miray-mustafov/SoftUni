function returnBiggerHalf(nums)
{
    let sorted_nums = nums.sort((a, b) => a-b)

    let result = sorted_nums.slice(Math.floor(sorted_nums.length/2) ,sorted_nums.length)
    return result
}


//retrunBiggerHalf([4, 7, 2, 5])
console.log(returnBiggerHalf([3, 19, 14, 7, 2, 19, 6]))