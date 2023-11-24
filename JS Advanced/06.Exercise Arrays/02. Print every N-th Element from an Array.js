function printNth(listt, nth){
    let result = []
    for (let i= 0; i< listt.length; i+=nth) {
        result.push(listt[i])
    }
    console.log(result)
}

printNth(['dsa',
'asd', 
'test', 
'tset'], 
2
)