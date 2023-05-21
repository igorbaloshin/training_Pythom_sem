# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной


#--------------------------------------------------------


# def open_file(filename):
#     with open('telephone_directory.txt', 'a', encoding='utf-8') as file:
#         file.write(input('Введите фамилию:') + '\n')
# def read_file(filename):
#     with open(r'telephone_directory.txt', 'r', encoding='utf-т8') as file:
#         for line in file:
#             print(line.strip())
# def user_actions():
#     if input('Read telephone directory?') == 'y':
#         return read_file('telephone_directory.txt')
        
#     if input('Write telephone directory?') == 'y':
#         return open_file('telephone_directory')
# user_actions()

#---------------------------------------------------------



from os import path

file_base = "base.txt"
all_data = []
last_id = 0

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    global all_data, last_id

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])
            return all_data
        return []


def show_all():
    if all_data:
        print(*all_data, sep="\n")
    else:
        print("Empty base!\n")


def main_menu():
    work = True
    while work:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all\n"
                       "2. Add\n"
                       "3. Search\n"
                       "4. Change\n"
                       "5. Delete\n"
                       "6. Exp/Imp\n"
                       "7. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
            case "7":
                work = False
            case _:
                print("Try again!\n")


main_menu()