# Задание 11: lambda-функции
numbers = [-10, 3, -2, 8, -5]
print("Исходный список:", numbers)
print("Обычная сортировка sorted():", sorted(numbers))
print("Сортировка по абсолютному значению:", sorted(numbers, key=lambda x: abs(x)))
print("lambda x: abs(x) задаёт ключ сортировки; сам список не меняется")
