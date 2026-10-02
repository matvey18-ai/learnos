# Задание 10: возврат нескольких значений (кортеж)
def analyze(numbers):
    minimum = numbers[0]
    maximum = numbers[0]
    total = 0
    for n in numbers:
        if n < minimum:
            minimum = n
        if n > maximum:
            maximum = n
        total = total + n
    average = total / len(numbers)
    return minimum, maximum, average


numbers = [5, 8, 2, 10, 4, 7]
minimum, maximum, average = analyze(numbers)
print("Список:", numbers)
print("Минимум:", minimum)
print("Максимум:", maximum)
print("Среднее:", average)
