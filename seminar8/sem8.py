def load_contacts(filename):#Загружает контакты из текстового файла.
    contacts = []
    with open(filename, "r", encoding ='utf-8') as f: #Имя файла.
        for line in f:
            name, surname, patronymic, phone_number = line.strip().split(",")
            contacts.append((name, surname, patronymic, phone_number))
    return contacts #Список контактов.

def save_contacts(filename, contacts):#Сохраняет контакты в текстовый файл.
    with open(filename, "w", encoding ='utf-8') as f: #Имя файла.
        for contact in contacts:
            f.write(",".join(contact) + "\n")#Список контактов.

def add_contact(contacts, name, surname, patronymic, phone_number):#Добавляет контакт.
  
    contacts.append((name, surname, patronymic, phone_number))

def find_contacts(contacts, search_term): # Находит контакты по имени, фамилии или отчеству.  
    found_contacts = []
    for contact in contacts:
        if search_term.lower() in "".join(contact).lower():
            found_contacts.append(contact)
    return found_contacts #Список найденных контактов.

def print_contacts(contacts): #Выводит все контакты.
    for contact in contacts:
        print(f"Имя: {contact[0]}")
        print(f"Фамилия: {contact[1]}")
        print(f"Отчество: {contact[2]}")
        print(f"Номер телефона: {contact[3]}")
        print()
        
def edit_contact(contacts, name, surname, new_name, new_surname, new_patronymic, new_phone_number): #Изменяет контакт.
    for i, contact in enumerate(contacts):
        if contact[0] == name and contact[1] == surname:
            contacts[i] = (new_name, new_surname, new_patronymic, new_phone_number)
            break

def delete_contact(contacts, name, surname):#Удаляет контакт.
    for i, contact in enumerate(contacts):
        if contact[0] == name and contact[1] == surname:
            del contacts[i]
            break

# Пример использования
filename = "contacts.txt"

# Загрузка контактов
contacts = load_contacts(filename)

# Вывод всех контактов
print_contacts(contacts)

# Добавление нового контакта
add_contact(contacts, "Иван", "Петров", "Сидорович", "+7 (900) 123-45-67")

# Поиск контактов
search_term = "Петров"
found_contacts = find_contacts(contacts, search_term)
print(f"Найдено {len(found_contacts)} контактов по запросу '{search_term}':")
for contact in found_contacts:
  print_contacts([contact])

# Сохранение контактов
save_contacts(filename, contacts)