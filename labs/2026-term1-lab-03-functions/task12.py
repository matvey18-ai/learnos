# Задание 12: самостоятельная работа - анализ результатов измерений
# В calculate_average, find_minimum, find_maximum встроенные
# sum(), min(), max() НЕ используются - алгоритмы реализованы вручную.
measurements = [4.5, 7.2, 3.1, 9.8, 5.6, 6.4, 2.7, 8.9, 5.0, 7.7, 6.1, 4.9]


def calculate_average(values):
    total = 0
    for v in values:
        total = total + v
    return total / len(values)


def find_minimum(values):
    smallest = values[0]
    for v in values[1:]:
        if v < smallest:
            smallest = v
    return smallest


def find_maximum(values):
    largest = values[0]
    for v in values[1:]:
        if v > largest:
            largest = v
    return largest


def count_above_average(values):
    average = calculate_average(values)
    count = 0
    for v in values:
        if v > average:
            count = count + 1
    return count


def find_value(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1


def analyze_measurements(values):
    return find_minimum(values), find_maximum(values), calculate_average(values)


minimum, maximum, average = analyze_measurements(measurements)
target = float(input("Введите значение для поиска: "))
index = find_value(measurements, target)

print("Количество измерений:", len(measurements))
print("Минимальное значение:", minimum)
print("Максимальное значение:", maximum)
print("Среднее значение:", average)
print("Значений выше среднего:", count_above_average(measurements))
if index >= 0:
    print(f"Значение {target} найдено, индекс {index}")
else:
    print(f"Значение {target} не найдено (результат find_value = {index})")
