try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    result = num1 / num2
    print(f"Результат деления: {result}")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль.")

try:
    number = int(input("Введите число: "))
    print(f"Вы ввели число: {number}")
except ValueError:
    print("Ошибка: Введено некорректное значение, это не число.")

try:
     with open("data.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Ошибка: Файл не найден.")

my_list = [1, 2, 3, 4, 5]
try:
    index = int(input("Введите индекс для доступа к элементу: "))
    print(f"Элемент списка: {my_list[index]}")
except IndexError:
    print("Ошибка: Индекс выходит за пределы списка.")

try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    operation = input("Введите операцию (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    else:
        raise ValueError("Неизвестная операция")

    print(f"Результат: {result}")

except ZeroDivisionError:
    print("Ошибка: Деление на ноль недопустимо.")
except ValueError as e:
    print(f"Ошибка: {e}")

while True:
    try:
        float_number = float(input("Введите число с плавающей запятой: "))
        print(f"Вы ввели число: {float_number}")
        break
    except ValueError:
        print("Ошибка: Введено некорректное значение, попробуйте снова.")

my_dict = {"a": 1, "b": 2, "c": 3}
key = input("Введите ключ для доступа: ")

try:
    print(f"Значение по ключу '{key}': {my_dict[key]}")
except KeyError:
    print("Ошибка: Ключа нет в словаре.")

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Ошибка: Деление на ноль недопустимо."

result = safe_divide(10, 0)
print(result)

filename = input("Введите имя файла: ")

try:
    with open(filename, "r") as file:
        number = int(file.read())
        print(f"Число из файла: {number}")
except FileNotFoundError:
    print("Ошибка: Файл не найден.")
except ValueError:
    print("Ошибка: В файле некорректное значение.")

try:
    number = float(input("Введите число: "))
    result = 100 / number
    result_int = int(result)
    print(f"Результат: {result_int}")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль недопустимо.")
except ValueError:
    print("Ошибка: Введено некорректное значение, это не число.")

