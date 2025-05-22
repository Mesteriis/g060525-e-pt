# Напишите функцию, которая принимает на вход строку и возвращает ее длину.
# Пример:
# Ввод: "Hello, World!"
# Вывод: 13


def string_length(s):
    """
    Функция принимает строку и возвращает ее длину.

    :param s: Входная строка
    :return: Длина строки
    """
    return len(s)

# Пример использования функции
if __name__ == "__main__":
    input_string = "Hello, World!"
    length = string_length(input_string)
    print(f"Длина строки '{input_string}' составляет {length} символов.")