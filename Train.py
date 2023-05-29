# print(*[i if i % 2 == 0 else '' for i in range(int(input("Введите число :")))])

# print(*[i * 2 for i in range(10) if i % 2 == 0])

# str = list("asfe")
# print(str)
# arr = []
# for i in range(5):
#     arr[i] = i
# print(arr)
#--------------------------------------------------------------------------
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
#----------------------------------------------------------------------------------

from os import path

file_base = 'telephon_base.txt'

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass



def open_file(filename):
    with open(filename , 'a' , encoding = 'utf-8') as f:
        f.write(input('Введите данные в формате  ФИ тел :') + '\n')
    
        
        
def read_file(filename):
    with open(filename, 'r', encoding='utf-8' )as f:
        for line in f:
            print(line)
                


       
open_file('telephon_base.txt')
read_file('telephon_base.txt')
