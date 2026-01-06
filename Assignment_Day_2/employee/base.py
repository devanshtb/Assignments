from abc import ABC, abstractmethod
from exceptions import InvalidEmployeeDataError


class Employee(ABC):
    def __init__(self, name: str, base_salary: float):
        if base_salary < 0:
            raise InvalidEmployeeDataError("Base salary cannot be negative")
        self.name = name
        self._base_salary = base_salary  # protected

    @property
    def base_salary(self):
        return self._base_salary

    @base_salary.setter
    def base_salary(self, value: float):
        if value < 0:
            raise InvalidEmployeeDataError("Base salary cannot be negative")
        self._base_salary = value

    @abstractmethod
    def calculate_salary(self) -> float:
        pass
