# Задание 7: встроенные функции для последовательностей
numbers = [5, 8, 2, 10, 4]
print("Список:", numbers)
print("Количество (len):", len(numbers))
print("Сумма (sum):", sum(numbers))
print("Минимум (min):", min(numbers))
print("Максимум (max):", max(numbers))
print("Среднее:", sum(numbers) / len(numbers))

sorted_copy = sorted(numbers)
print("sorted() -> новый список:", sorted_copy, "| исходный не изменился:", numbers)

numbers.sort()
print("list.sort() -> список изменён на месте:", numbers)
