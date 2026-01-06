from employee.base import Employee
from exceptions import SalaryCalculationError


class FullTimeEmployee(Employee):
    def __init__(self, base_salary: float, bonus: float = 5000):
        super().__init__("FullTimeEmployee", base_salary)
        self.bonus = bonus

    def calculate_salary(self) -> float:
        salary = self.base_salary + self.bonus
        if salary < 0:
            raise SalaryCalculationError("Invalid full-time salary calculation")
        return salary
