function etrem(){
    console.log(1)
    console.log(this)
}

let context = 2
etrem.bind(context)

etrem()
let a = 5