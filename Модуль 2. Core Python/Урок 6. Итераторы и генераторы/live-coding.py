# # Тема: Вложенные циклы: for вложенный в for, for вложенный в while.
# # Покажите и объясните использования вложенных циклов в формате live-coding.
#
# # matrix = [
# #     [1, 2, 3],
# #     [4, 5, 6],
# #     [7, 8, 9]
# # ]
# # for row in matrix:
# #     for element in row:
# #         print(element, end=' ')
# #     print()  # Переход на новую строку после вывода всех элементов строки
# #
# #
# # numbers = [1, 2, 3, 4, 5]
# # for i in range(1, 4):  # Внешний цикл
# #     for j in numbers:  # Внутренний цикл
# #         print(f"Внешний цикл: {i}, Внутренний цикл: {j}")
# #     print("Конец итерации внешнего цикла")  # Переход на новую строку после завершения внутреннего цикла
#
#
#
# # Тема: Генераторы списков (List comprehension). Вложенные циклы и вложенные генераторы списков.
#
#
# # Продемонстрируйте и объясните использование генераторов списков.
# # В том числе использование вложенных генераторов списков.
#
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = [x**2 for x in numbers]  # Генератор списка для возведения в квадрат
# print("Квадраты чисел:", squared_numbers)
# # Вложенный генератор списка для создания матрицы
# matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
# squared_matrix = [[x**2 for x in row] for row in matrix]  # Генератор списка для возведения в квадрат
#
# print(matrix)
# print(squared_matrix)
#

# Тема: Итератор и итерируемые объекты. Функции iter и next. Сравнение iter и next с циклом for и функцией range.
# Продемонстрируйте создание итератора и использование функций iter и next.

numbers = [1, 2, 3, 4, 5, 6]

# Создание итератора
iterator = iter(numbers)
# print(type(iterator))  # <class 'list_iterator'>
# Использование функции next для получения следующего элемента
count = 0
while True:
    try:
        pair = next(iterator), next(iterator), next(iterator)
        print(f"Следующий элемент: {pair}")
        if count == 2:
            print("Прерывание итерации на третьем элементе")
            break
    except StopIteration:
        print("Итератор завершен")
        break


