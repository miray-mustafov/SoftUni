const {calc} = require('./calculator')
const {expect}=require('chai')
let c = calc()

describe('sokemaaa',()=>{
    it('tst1',()=>{
        expect(c.add(1) ,c.get()).to.eq(1)
    })
})