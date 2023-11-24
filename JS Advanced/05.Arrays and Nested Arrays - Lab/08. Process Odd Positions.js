function solve(nums){
    let odd = nums.filter((x,i) => i % 2 )
    const doubled = odd.map(x=>x*2)
    doubled.reverse();

    console.log(...doubled)
}

solve([10, 15, 20, 25]) // 50 30
solve([3, 0, 10, 4, 7, 3]) // 6 8 0