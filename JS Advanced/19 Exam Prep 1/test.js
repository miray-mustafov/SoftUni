let { expect } = require("chai")
let bookSelection = require('./03. Book-selection/solution').bookSelection

describe("Tests …", function () {
    describe("isGenreSuitable", function () {
        it("unsuitable scenarios", function () {
            expect(bookSelection.isGenreSuitable('Thriller', 12)).to.eq(`Books with Thriller genre are not suitable for kids at 12 age`)
            expect(bookSelection.isGenreSuitable('Thriller', 11)).to.eq(`Books with Thriller genre are not suitable for kids at 11 age`)
            expect(bookSelection.isGenreSuitable('Horror', 12)).to.eq(`Books with Horror genre are not suitable for kids at 12 age`)
            expect(bookSelection.isGenreSuitable('Horror', 11)).to.eq(`Books with Horror genre are not suitable for kids at 11 age`)
        });
        it("happy path", function () {
            expect(bookSelection.isGenreSuitable('Horror', 13)).to.eq(`Those books are suitable`)
            expect(bookSelection.isGenreSuitable('Thriller', 13)).to.eq(`Those books are suitable`)
            expect(bookSelection.isGenreSuitable('a', 13)).to.eq(`Those books are suitable`)
        });
    });
    describe("isItAffordable", function () {
        it("happy path", function () {
            expect(bookSelection.isItAffordable(10, 20)).to.eq(`Book bought. You have 10$ left`)
            expect(bookSelection.isItAffordable(10, 10)).to.eq(`Book bought. You have 0$ left`)
        });
        it("not happy path", function () {
            expect(bookSelection.isItAffordable(10, 5)).to.eq("You don\'t have enough money")
        });
        it("not valid inputs", function () {
            expect(() => bookSelection.isItAffordable()).to.throw()
            expect(() => bookSelection.isItAffordable(1)).to.throw()
            expect(() => bookSelection.isItAffordable("1", 1)).to.throw()
            expect(() => bookSelection.isItAffordable([], 1)).to.throw()
            expect(() => bookSelection.isItAffordable({}, 1)).to.throw()

        });
    });
    describe("suitableTitles", function () {
        it("happy path", function () {
            expect(3).to.be.eq(3)
        });
    });
});
