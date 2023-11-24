function solve(area_, vol_, cubes_params) {
    cubes_params = JSON.parse(cubes_params)
    r = []

    for (let cube of cubes_params) {
        let result_area = area_.call(cube)
        let result_vol = vol_.call(cube)
        r.push({area: result_area, volume: result_vol})    
    }
    
    return r
};



function area() {
    return Math.abs(this.x * this.y);
};
function vol() {
    return Math.abs(this.x * this.y * this.z);
};

solve(area, vol, `[
    {"x":"1","y":"2","z":"10"},
    {"x":"7","y":"7","z":"10"},
    {"x":"5","y":"2","z":"10"}
    ]`
    )