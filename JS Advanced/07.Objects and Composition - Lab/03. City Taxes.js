function collectTaxes(){
    this.treasury += Math.floor(this.population * this.tax_rate)
}
function applyGrowth(percentage){
    this.population += Math.floor(this.population*percentage/100)
}
function applyRecession(percentage){
    this.treasury -= Math.floor(this.treasury * percentage/100  )
} 

function cityTaxes(name, population, treasury)
{
    const result = {
        name,
        population,
        treasury,
        tax_rate: 10,
        collectTaxes,
        applyGrowth,
        applyRecession
    }

    return result
}

const city =
  cityTaxes('Tortuga',
  7000,
  15000);
city.collectTaxes();
console.log(city.treasury);
city.applyGrowth(5);
console.log(city.population);
