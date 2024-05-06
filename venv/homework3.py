
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []
    def add_employee(self, employee):
        self.employees.append(employee)
    def remove_employee(self, employee):
        self.employees.remove(employee)
    def get_total_salary(self):
        total_salary = 0
        for employee in self.employees:
            total_salary += employee.salary
        return total_salary
