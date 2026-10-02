# Задание 9: линейный поиск
def find_element(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1


numbers = [14, 3, 27, 8, 21, 5]
print("Список:", numbers)
print("Индекс числа 21 (есть в списке):", find_element(numbers, 21))
print("Индекс числа 99 (нет в списке): ", find_element(numbers, 99))
