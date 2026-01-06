import sys
import os
from datetime import datetime

from employee.full_time import FullTimeEmployee
from employee.part_time import PartTimeEmployee
from utils.helpers import (
    generate_random_employees,
    calculate_salaries,
    filter_high_earners,
    calculate_total_payroll,
)
from exceptions import InvalidEmployeeDataError, SalaryCalculationError


def validate_environment():
    if "PYTHONPATH" not in os.environ:
        print("Warning: PYTHONPATH not set")


def parse_arguments(args):
    employees = []
    i = 0
    while i < len(args):
        if args[i] == "full_time":
            employees.append(FullTimeEmployee(float(args[i + 1])))
            i += 2
        elif args[i] == "part_time":
            employees.append(
                PartTimeEmployee(float(args[i + 1]), int(args[i + 2]))
            )
            i += 3
        else:
            raise InvalidEmployeeDataError("Unknown employee type")
    return employees


def main():
    validate_environment()
    print(f"Execution Time : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    try:
        if len(sys.argv) > 1:
            employees = parse_arguments(sys.argv[1:])
        else:
            employees = generate_random_employees()

        salaries = calculate_salaries(employees)

        print("\nEmployee List:")
        for emp, salary in zip(employees, salaries):
            print(f"- {emp.name} : Salary = {salary}")

        high_earners = filter_high_earners(employees, 20000)

        print("\nFiltered Employees (Salary > 20000):")
        for emp in high_earners:
            print(f"- {emp.name}")

        total_payroll = calculate_total_payroll(employees)
        print(f"\nTotal Payroll Amount : {total_payroll}")

    except (InvalidEmployeeDataError, SalaryCalculationError) as error:
        print(f"Error: {error}")

    finally:
        print("\nProgram finished execution.")


if __name__ == "__main__":
    main()
