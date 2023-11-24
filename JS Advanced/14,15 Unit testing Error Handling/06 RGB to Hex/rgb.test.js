const {rgbToHexColor} = require('./rgb')
const {expect} = require('chai')

describe("test if it:", ()=>{
    it('returns correct black white and random',()=>{
        expect(rgbToHexColor(0,0,0)).equal('#000000');
        expect(rgbToHexColor(255,255,255)).equal('#FFFFFF');
        expect(rgbToHexColor(1,1,1)).equal('#010101');
    } )
    it('returs undefined if incorrect input',()=>{
        expect(rgbToHexColor(1,1,256)).to.be.undefined;
        expect(rgbToHexColor(-1,4,2)).to.be.undefined;
        expect(rgbToHexColor(1,1)).to.be.undefined;
        expect(rgbToHexColor(1,)).to.be.undefined;
        expect(rgbToHexColor()).to.be.undefined;
        expect(rgbToHexColor(1,"1",2)).to.be.undefined;
    } )
})