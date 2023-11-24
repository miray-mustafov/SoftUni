class Garden {
    constructor(spaceAvailable) {
        this.spaceAvailable = spaceAvailable
        this.plants = []
        this.storage = []
    }

    addPlant(plantName, spaceRequired) {// string, num
        if (this.spaceAvailable < spaceRequired) {
            throw new Error("Not enough space in the garden.")
        }
        this.spaceAvailable -= spaceRequired
        this.plants.push({ plantName, spaceRequired, ripe: false, quantity: 0 });
        return `The ${plantName} has been successfully planted in the garden.`
    }

    ripenPlant(plantName, quantity) {
        let current_plant = this.plants.find(x => x.plantName == plantName)
        if (!current_plant) {
            throw new Error(`There is no ${plantName} in the garden.`);
        }
        if (current_plant.ripe) {
            throw new Error(`The ${plantName} is already ripe.`);
        }
        if (quantity <= 0) {
            throw new Error("The quantity cannot be zero or negative.")
        }
        current_plant.ripe = true;
        current_plant.quantity += quantity;

        if (quantity == 1) {
            return `${quantity} ${plantName} has successfully ripened.`;
        } else {
            return `${quantity} ${plantName}s have successfully ripened.`;
        }
    }

    harvestPlant(plantName) {
        let current_plant = this.plants.find(x => x.plantName == plantName)
        if (!current_plant) {
            throw new Error(`There is no ${plantName} in the garden.`)
        }
        if (!current_plant.ripe) {
            throw new Error(`The ${plantName} cannot be harvested before it is ripe.`)
        }
        this.storage.push({ plantName, quantity: current_plant.quantity })
        this.spaceAvailable += current_plant.spaceRequired
        this.plants = this.plants.filter(x => x.plantName != plantName)

        return `The ${plantName} has been successfully harvested.`
    }
    generateReport(){
        let report = `The garden has ${ this.spaceAvailable } free space left.\n`;
        let sorted_plants = this.plants.sort((a,b)=>
            a.plantName.localeCompare(b.plantName));
        sorted_plants = sorted_plants.map(x=>x.plantName)
            .join(', ');
        report += `Plants in the garden: ${sorted_plants}\n`  
        
        if (this.storage === []) {
            report += "Plants in storage: The storage is empty."
        }else{
            let name_quantity = this.storage.map(x => `${x.plantName} (${x.quantity})`) 
            report += `Plants in storage: ${name_quantity.join(', ')}`
        } 
        
        return report
    }

}
// test 6
const myGarden = new Garden(250)
console.log(myGarden.addPlant('apple', 20));
console.log(myGarden.addPlant('orange', 10));
//console.log(myGarden.addPlant('raspberry', 10));
console.log(myGarden.ripenPlant('apple', 10));
console.log(myGarden.ripenPlant('apple', 10));
console.log(myGarden.ripenPlant('orange', 1));
console.log(myGarden.harvestPlant('orange'));
console.log(myGarden.harvestPlant('apple'));
console.log(myGarden.generateReport());


