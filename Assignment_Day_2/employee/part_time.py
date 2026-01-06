from employee.base import Employee
from exceptions import InvalidEmployeeDataError, SalaryCalculationError


class PartTimeEmployee(Employee):
    def __init__(self, hourly_rate: float, hours_worked: int):
        if hourly_rate < 0 or hours_worked < 0:
            raise InvalidEmployeeDataError("Hourly rate and hours must be positive")
        super().__init__("PartTimeEmployee", 0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self) -> float:
        salary = self.hourly_rate * self.hours_worked
        if salary < 0:
            raise SalaryCalculationError("Invalid part-time salary calculation")
        return salary
