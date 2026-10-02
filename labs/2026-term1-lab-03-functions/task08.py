# Задание 8: собственные алгоритмы без sum(), min(), max()
def calculate_sum(numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total


def find_min(numbers):
    smallest = numbers[0]
    for n in numbers[1:]:
        if n < smallest:
            smallest = n
    return smallest


def find_max(numbers):
    largest = numbers[0]
    for n in numbers[1:]:
        if n > largest:
            largest = n
    return largest


numbers = [5, 8, 2, 10, 4]
print("Список:", numbers)
print("calculate_sum:", calculate_sum(numbers), "| встроенный sum:", sum(numbers))
print("find_min:     ", find_min(numbers), "| встроенный min:", min(numbers))
print("find_max:     ", find_max(numbers), "| встроенный max:", max(numbers))
