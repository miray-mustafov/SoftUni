function countNeighbours(matrix)
{    
    let counter = 0;
    for (let row_i = 0; row_i < matrix.length; row_i++) {
        for (let col_i = 0; col_i < matrix[0].length; col_i++) {
            
            if (row_i !== matrix.length - 1) {
                if(matrix[row_i][col_i]===matrix[row_i + 1][col_i]){
                counter+=1;      
                }
            }

            if(matrix[row_i][col_i]===matrix[row_i][col_i + 1]){
                counter+=1;      
            }
        }
        


    }
    return counter
    console.log(counter)
}


countNeighbours([['test', 'yes', 'yo', 'ho'],
['well', 'done', 'yo', 'ho'],
['not', 'done', 'yet', 'yet']]
)                