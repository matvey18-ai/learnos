# Задание 3: области видимости переменных
value = 10


def example():
    value = 20
    print("Внутри функции value =", value)


example()
print("Снаружи функции value =", value)


# Дополнение: локальная переменная и попытка обращения после вызова функции
def demo():
    local_only = 42
    print("Внутри demo() local_only =", local_only)


demo()
print("Обращение к local_only после вызова:", local_only)
