# Задание 6: работа с кортежами
measurements = (4.1, 5.2, 3.8, 6.0, 7.1, 2.9, 8.3, 5.5)
print("Кортеж measurements:", measurements)
print("Первый элемент:", measurements[0])
print("Последний элемент:", measurements[-1])
print("Срез первых трёх:", measurements[0:3])

# Попытка изменить элемент кортежа -> TypeError (фиксируем ошибку)
try:
    measurements[0] = 99.0
except TypeError as error:
    print("Ошибка при изменении кортежа:", error)

# Распаковка первых двух значений
first, second, *rest = measurements
print("Распаковка: first =", first, "| second =", second, "| остальных:", len(rest))

# Преобразование: кортеж -> список -> правка -> кортеж
as_list = list(measurements)
as_list[0] = 99.9
measurements_fixed = tuple(as_list)
print("tuple -> list -> tuple:", measurements_fixed)
print("Проверка типа:", type(measurements_fixed))
