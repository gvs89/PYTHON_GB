def display_contacts():
    with open("contacts.txt", "r") as file:
        contacts = file.readlines()
        for contact in contacts:
            print(contact.strip())


def add_contact():
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone = input("Введите номер телефона: ")

    with open("contacts.txt", "a") as file:
        file.write(f"{surname}, {name}, {patronymic}, {phone}\n")
    print("Контакт успешно добавлен!")


def delete_contact():
    search_term = input("Введите фамилию или имя для удаления: ")
    found = False
    with open("contacts.txt", "r") as file:
        lines = file.readlines()
    with open("contacts.txt", "w") as file:
        for line in lines:
            if search_term.lower() not in line.lower():
                file.write(line)
            else:
                found = True
    if found:
        print("Контакт успешно удален!")
    else:
        print("Контакт не найден.")


def modify_contact():
    search_term = input("Введите фамилию или имя для изменения: ")
    found = False
    with open("contacts.txt", "r") as file:
        lines = file.readlines()
    with open("contacts.txt", "w") as file:
        for line in lines:
            if search_term.lower() not in line.lower():
                file.write(line)
            else:
                found = True
                surname, name, patronymic, phone = line.strip().split(", ")
                print("Текущие данные:")
                print(f"Фамилия: {surname}")
                print(f"Имя: {name}")
                print(f"Отчество: {patronymic}")
                print(f"Номер телефона: {phone}")
                print("Введите новые данные (оставьте пустым для оставления без изменения):")
                new_surname = input(f"Новая фамилия ({surname}): ") or surname
                new_name = input(f"Новое имя ({name}): ") or name
                new_patronymic = input(f"Новое отчество ({patronymic}): ") or patronymic
                new_phone = input(f"Новый номер телефона ({phone}): ") or phone
                file.write(f"{new_surname}, {new_name}, {new_patronymic}, {new_phone}\n")
    if found:
        print("Контакт успешно изменен!")
    else:
        print("Контакт не найден.")


def export_contacts():
    with open("contacts.txt", "r") as file:
        contacts = file.read()
    with open("exported_contacts.txt", "w") as file:
        file.write(contacts)
    print("Контакты успешно экспортированы в файл exported_contacts.txt")


def import_contacts():
    try:
        with open("imported_contacts.txt", "r") as file:
            imported_contacts = file.readlines()
        with open("contacts.txt", "a") as file:
            file.writelines(imported_contacts)
        print("Контакты успешно импортированы из файла imported_contacts.txt")
    except FileNotFoundError:
        print("Файл imported_contacts.txt не найден.")


def main():
    while True:
        print("\nМеню:")
        print("1. Вывести контакты")
        print("2. Добавить контакт")
        print("3. Удалить контакт")
        print("4. Изменить контакт")
        print("5. Экспорт контактов")
        print("6. Импорт контактов")
        print("7. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            display_contacts()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            modify_contact()
        elif choice == "5":
            export_contacts()
        elif choice == "6":
            import_contacts()
        elif choice == "7":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 7.")


if __name__ == "__main__":
    main()
