# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал для изменения и удаления данных.



from os import path

file_base = "telephon_book.txt"
all_data = []
last_id = 0

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    
    global all_data, last_id

    with open(file_base, "r", encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])

        return all_data


def show_all():
    
    if not all_data:
        print("Empty base")
    else:
        print(*all_data, sep="\n")


def add_contact():
    

    global last_id

    array = ['Фамилию', 'Имя', 'Отчество', 'номер телефона']
    answers = []
    for i in array:
        answers.append(data_collection(i))

    if not exist_contact(0, " ".join(answers)):
        last_id += 1
        answers.insert(0, str(last_id))

        with open(file_base, 'a', encoding="utf-8") as f:
            f.write(f'{" ".join(answers)}\n')
        print("Запись добавлена\n")
    else:
        print("Запись уже существует")


def del_contact():
    
    global all_data

    symbol = "\n"
    show_all()
    del_record = input("Введите id абонента: ")

    if exist_contact(del_record, ""):
        all_data = [k for k in all_data if k.split()[0] != del_record]

        with open(file_base, 'w', encoding="utf-8") as f:
            f.write(f'{symbol.join(all_data)}\n')
        print("Запись удалена!\n")
    else:
        print("Данные некорректны!")


def exist_contact(rec_id, data):
    
    if rec_id:
        candidates = [i for i in all_data if rec_id in i.split()[0]]
    else:
        candidates = [i for i in all_data if data in i]
    return candidates


def data_collection(num):
   

    answer = input(f"Введите {num}: ")
    while True:
        if num in "Фамилию Имя Отчество":
            if answer.isalpha():
                break
        if num == "номер телефона":
            if answer.isdigit() and len(answer) <= 11:
                break
        answer = input(f"Данные некорректны!\n"
                       f"Используете буквы алфавита, "
                       f"Номер до 11 цифр\n"
                       f"Введите {num}: ")
    return answer


def main_menu():
    
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Показать книгу\n"
                       "2. Добавить запись\n"
                       "3. Удалить запись\n"
                       "4. Выход\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_contact()            
            case "3":
                del_contact()
            case "4":
                play = False
            case _:
                print("Попробуйте еще!\n")



main_menu()

