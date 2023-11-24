function ex1 (input){
    let emptyString = ``

    for (const line of input) {
        let [command,arg] = line.split(' ')

        if(command==`Add`){
            emptyString+=arg
         }
        else if(command==`Print`){
            console.log(emptyString)
         }
        else if(command==`Upgrade`){
           if(emptyString.includes(arg)){
            let code = arg.charCodeAt(0)
            let char = String.fromCharCode(code+1)
                emptyString = emptyString.replace(arg, char)
           }
         }
        else if(command==`Index`){
            if(emptyString.includes(arg)){
                let stringy = ``
                for(i=0 ; i<emptyString.length ; i++){
                    if(emptyString[i]==arg){
                        stringy+=i+` `
                    }
                }
                console.log(stringy)
            }else{
                console.log('None')
            }
         }
        else if(command==`Remove`){

            let reg = new RegExp(arg, "gi");
            emptyString = emptyString.replace(reg,'')

         }
         if(command==`End`){
            break
         }

    }
}

ex1([
"Add HelloW12orld",
"Upgrade e",
"Index ll",
"Remove rl",
"Print",
"End"])