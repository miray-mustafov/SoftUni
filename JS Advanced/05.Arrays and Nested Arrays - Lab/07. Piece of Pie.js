function cake(pies, start_pie, end_pie)
{
    
    let i = 0;
    let start_idx = undefined
    let end_idx = undefined

    
    for (; i < pies.length; i++) {

        if(pies[i] === start_pie){
            start_idx = i
        }
    }

    for (i = start_idx; i < pies.length; i++) {
        
        if(pies[i] === end_pie){
            end_idx = i
        }
    }

    return pies.slice(start_idx,end_idx+1)
}

console.log(cake(['Pumpkin Pie',
'Key Lime Pie',
'Cherry Pie',
'Lemon Meringue Pie',
'Sugar Cream Pie'],
'Key Lime Pie',
'Lemon Meringue Pie'
))
