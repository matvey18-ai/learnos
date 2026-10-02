# Задание 2: аргументы и возвращаемые значения
def calculate_rectangle(width, height):
    return width * height


def calculate_perimeter(width, height):
    return 2 * (width + height)


def describe_rectangle(width, height, unit="см"):
    print(
        f"Прямоугольник {width} x {height} {unit}: "
        f"площадь = {calculate_rectangle(width, height)} {unit}^2, "
        f"периметр = {calculate_perimeter(width, height)} {unit}"
    )


print("Площадь 5 x 3  =", calculate_rectangle(5, 3))
print("Периметр 5 x 3 =", calculate_perimeter(5, 3))
describe_rectangle(5, 3)                 # аргумент unit не передан -> "см"
describe_rectangle(2.5, 4, unit="м")     # аргумент unit передан явно
