const { expect } = require('chai')

let mathEnforcer = {
    addFive: function (num) {
        if (typeof(num) !== 'number') {
            return undefined;
        }
        return num + 5;
    },
    subtractTen: function (num) {
        if (typeof(num) !== 'number') {
            return undefined;
        }
        return num - 10;
    },
    sum: function (num1, num2) {
        if (typeof(num1) !== 'number' || typeof(num2) !== 'number') {
            return undefined;
        }
        return num1 + num2;
    }
};


describe('tst group', function() {
    describe('addfive', () => {
        it('if input NOT num', () => {
            expect(mathEnforcer.addFive('5')).to.equal(undefined);
            expect(mathEnforcer.addFive({})).to.equal(undefined);
            expect(mathEnforcer.addFive([1])).to.equal(undefined);
        })
        it('if input NOT num', () => {
            expect(mathEnforcer.addFive(5)).to.equal(10);
            expect(mathEnforcer.addFive(5.5)).to.equal(10.5);
        })
    })
    describe('subtactten', () => {
        it('1', () => {
        })
    })
    describe('sum', () => {
        it('1', () => {
        })
    })}
)
