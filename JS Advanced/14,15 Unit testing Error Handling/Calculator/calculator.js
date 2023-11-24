function calc() {
    let value = 0;
    return {
        add: function(num) { value += Number(num); },
        subtract: function(num) { value -= Number(num); },
        get: function() { return value; }
    }
}
let calc1 = calc()
calc1.add(1)
console.log(calc1.get())
module.exports = {calc}