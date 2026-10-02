# Задание 1: создание и вызов функций
def greet(name):
    print("Здравствуйте,", name)


def square(number):
    return number ** 2


def max_of_two(a, b):
    # без использования встроенной функции max()
    if a > b:
        return a
    return b


greet("Иван")
greet("Мария")
print("square(5)  =", square(5))
print("square(-3) =", square(-3))
print("max_of_two(5, 3)  =", max_of_two(5, 3))
print("max_of_two(-2, -7) =", max_of_two(-2, -7))
