# Homework 1
1.
a = input("Вкажіть своє ім'я:")
b = int(input("Вкажіть свій вік:"))
print("Привіт",a,"тобі",b,"років")

2.
age = int(input("Вкажіть свій вік:"))
if age >= 18:
    print("Вхід дозволено")
else:
    print("Вхід заборонено")

3.
import random
Number = random.randint(1, 10)
attempts = 3
for attempt in range(1, attempts + 1):
    guess = int(input("Вгадай число від 1 до 10: "))
    if guess == Number:
        print("Ви вгадали , це було число:",Number)
        break
    elif guess < Number:
        print("Більше")
    else:
        print("Менше")
else:
    print("Bи не вгадали , це було число:",Number)

4.
first = int(input("Введіть перше число: "))
second = int(input("Введіть друге число: "))
print(("Числа з"),first,("до"),second)
for number in range(first , second + 1):
    print(number)

5.
n = int(input("Число n: "))
print("Парні числа від 1 до n у зворотному порядку:")
for number in range(n, 0, -1):
    if number % 2 == 0:
        print(number, end=" ")

6.
n = int(input("Введіть число n: "))
factorial = 1
for number in range(1, n + 1):
    factorial *= number
print(("Факторіал числа"), (n),"=",(factorial))

7.
Mark = int(input("Введіть кількість балів від 0 до 100: "))
if 0 <= Mark and Mark <= 49:
    print("Оцінка: незадовільно.")
elif 50 <= Mark and Mark <= 69:
    print("Оцінка: задовільно.")
elif 70 <= Mark and Mark <= 89:
    print("Оцінка: добре.")
elif 90 <= Mark and Mark <= 100:
    print("Оцінка: відмінно.")
else:
    print("Виберіть число від 0 до 100")

8.
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
c = input("Введіть дію (+, -, *, /): ")
if c == '+':
    result = a + b
    print(result)
elif c == '-':
    result = a - b
    print(result)
elif c == '*':
    result = a * b
    print(result)
elif c == '/':
    result = a / b
    print(result)
    if b == 0:
        print("Ділення на нуль")


