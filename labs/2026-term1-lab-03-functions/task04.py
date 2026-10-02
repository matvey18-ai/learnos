# Задание 4: работа со списками
numbers = [12, 7, 31, 4, 19, 25, 3, 40, 16, 9]
print("Исходный список:", numbers)

print("Первый элемент:", numbers[0])
print("Третий элемент:", numbers[2])
print("Последний элемент:", numbers[-1])

numbers[1] = 70
print("После изменения второго элемента:", numbers)

numbers.append(55)
print("После append(55):", numbers)

numbers.remove(31)
print("После remove(31):", numbers)

extracted = numbers.pop()
print("После pop(), извлечено:", extracted)
print("Итоговый список:", numbers)
print("Количество элементов len():", len(numbers))
