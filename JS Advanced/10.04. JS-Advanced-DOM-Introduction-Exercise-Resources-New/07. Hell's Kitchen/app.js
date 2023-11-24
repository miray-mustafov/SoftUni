function solve() {
   document.querySelector('#btnSend').addEventListener('click', onClick);


   function onClick() {
      let input_jsarr = JSON.parse(document.getElementsByTagName('textarea')[0].value)
      let best_restaurant;
      let best_avg_sal = -10000.00;
      let restaurants_obj = {}

      for (let el of input_jsarr) {
         let [restaurant_name, workers] = el.split(' - ')
         let workers_obj = {}

         for (let worker of workers.split(', ')) {
            let [name, salary] = worker.split(' ')
            workers_obj[name] = Number(salary)
         }


         if (!restaurants_obj.hasOwnProperty(restaurant_name)) {
            restaurants_obj[restaurant_name] = workers_obj
         }
         else {
            let new_workers_obj = { ...restaurants_obj[restaurant_name], ...workers_obj }
            restaurants_obj[restaurant_name] = new_workers_obj
         }

      }//{"Mikes":{"Steve":1000,"Ivan":200,"Paul":800,"Mirai":1200,"Mimi":600},"Fleet":

      for (let [name, workers_obj] of Object.entries(restaurants_obj)) {
         let salaries_arr = Object.values(workers_obj)
         let curr_avg_sal = (salaries_arr.reduce((a, b) => a + b, 0) / salaries_arr.length).toFixed(2)

         if (curr_avg_sal > best_avg_sal) {
            best_avg_sal = curr_avg_sal
            let sorted_workers = Object.entries(workers_obj).sort((a, b) => +b[1] - +a[1])
            let best_salary = salaries_arr.sort((a, b) => b - a)[0]
            best_restaurant = { name, best_avg_sal, best_salary, workers: sorted_workers }

         }
      }

      document.getElementById('bestRestaurant').getElementsByTagName('p')[0].textContent = `Name: ${best_restaurant.name} Average Salary: ${best_restaurant.best_avg_sal} Best Salary: ${best_restaurant.best_salary.toFixed(2)}`;

      let workers_maped = best_restaurant.workers.map(e => `Name: ${e[0]} With Salary: ${e[1]}`)
      document.getElementById('workers').getElementsByTagName('p')[0].textContent = workers_maped.join(' ')
   }
}