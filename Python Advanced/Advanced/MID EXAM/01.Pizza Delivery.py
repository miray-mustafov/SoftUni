from collections import deque

pizzas = deque([int(num) for num in input().split(', ') if 0 < int(num) <= 10])
pizzas_count = sum(pizzas)
employees = [int(emp) for emp in input().split(', ')]

while employees and pizzas:
    emp = employees.pop()
    pizza = pizzas[0]
    if emp >= pizza:
        pizzas.popleft()
    else:
        pizzas[0] -= emp

if pizzas:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(piz) for piz in pizzas])}")
else:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {pizzas_count}")
    print(f'Employees: {", ".join(str(emp) for emp in employees)}')
