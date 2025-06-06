# Проект: Управление библиотекой
#
# Описание:
# Разработайте программу для управления библиотекой. Программа должна позволять добавлять книги в библиотеку,
# удалять книги, искать книги по автору и выводить список всех книг с их авторами и статусами (в наличии или выдана).
#
# Требования: Реализуйте работу всех пунктов меню.

library = [["Война и мир", "Толстой", "в наличии"],
           ["Преступление и наказание", "Достоевский", "выдана"],
           ["Мастер и Маргарита", "Булгаков", "в наличии"]]

# while True:
#     print("\nМеню")
#     print("1. Показать список всех книг")
#     print("2. Добавить книгу")
#     print("3. Удалить книгу")
#     print("4. Поменять статус книги")
#     print("5. Показать книги определенного автора")
#     print("6. Показать книги с определенным статусом")
#     choice = input("Выберите действие, введя его номер: ")
#
#     # Продолжите программу ниже.
#
#     if choice == "1":
#         pass
#     if choice == "2":
#         pass

for el in library:
    print(f"{el[0]} - {el[1]} - {el[2]}")

    # for book in library:
    #     if book[0] == choice:
    #         library.remove(book)