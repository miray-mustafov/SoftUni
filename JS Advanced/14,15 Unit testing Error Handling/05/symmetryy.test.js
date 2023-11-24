const { expect } = require('chai')
const { isSymmetric } = require('./symmetryy')

describe('test group', () => {
    it('returns true if inp_arr is symm', ()=>{
        expect(isSymmetric([1,2,2,1])).to.be.true;
    })
    it('returns false with incorrect data type', ()=>{
        expect(isSymmetric([1,2,2,'1'])).to.be.false;
        expect(isSymmetric(1221)).to.be.false;
        expect(isSymmetric('1221')).to.be.false;
    })
})