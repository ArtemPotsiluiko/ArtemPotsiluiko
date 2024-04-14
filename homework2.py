1.
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    def deposit (self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
2.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def get_info(self):
        return f"[{self.year}] {self.make} {self.model}"

3.
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    def get_salary_info(self):
        return f"Заробітна плата {self.name}: {self.salary}"

4.
class Rectangle:
    def __init__(self, width,height):
        self.width = width
        self.height = height
        def calculate_area(self):
            return self.width * self.height
        def calculate_perimeter(self):
            return 2 * (self.width + self.height)

5.
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price * self.quantity
    def display_info(self):
        print(f"Товар: {self.name}")
        print(f"Ціна за одиницю: {self.price}")
        print(f"Кількість: {self.quantity}")
        total_price = self.calculate_total_price()
        print(f"Загальна вартість: {total_price}")
