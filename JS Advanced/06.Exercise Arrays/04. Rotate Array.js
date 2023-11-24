function rotateArr(arr, rotations)
{
    for (let i = 0; i < rotations; i++) {
        arr.unshift(arr.pop())
    }
    console.log(...arr)
}
rotateArr(['1', 
'2', 
'3', 
'4'], 
3
)
rotateArr(['Banana', 
'Orange', 
'Coconut', 
'Apple'], 
13
)

