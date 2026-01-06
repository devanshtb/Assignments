import random
from functools import reduce
from employee.full_time import FullTimeEmployee
from employee.part_time import PartTimeEmployee


def generate_random_employees(count: int = 2):
    employees = []
    for _ in range(count):
        if random.choice([True, False]):
            employees.append(
                FullTimeEmployee(base_salary=random.randint(30000, 70000))
            )
        else:
            employees.append(
                PartTimeEmployee(
                    hourly_rate=random.randint(100, 500),
                    hours_worked=random.randint(10, 50)
                )
            )
    return employees


def calculate_salaries(employees):
    return list(map(lambda emp: emp.calculate_salary(), employees))


def filter_high_earners(employees, threshold):
    return list(filter(lambda emp: emp.calculate_salary() > threshold, employees))


def calculate_total_payroll(employees):
    return reduce(lambda total, emp: total + emp.calculate_salary(), employees, 0)
