#  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод:                                     Вывод:
# пра-ра-раам рам-пам-папам па-ра-па-дам    Парам пам-пам
 
 
dic = {"АЕИОУЫЭЮЯ":1,
       "БВГДЖЗЙКЛМНПРСТФХЦЧШЩЬЪ":0,}

phrase_arr = list(input("Введите считалку :").upper().split(" "))

#print(phrase_arr)

phrase_arr_clean = [i.replace('-', '') for i in phrase_arr]

#print(phrase_arr_clean)

phrase_arr_clean_split = list(map(list,phrase_arr_clean))

print(phrase_arr_clean_split)

flag = 1 # Индикатор для печати

phrase_arr_count = []
for i in range(len(phrase_arr_clean_split)):
    Sum = 0
    check = 0
    for j in range(len(phrase_arr_clean_split[i])):
        
        for k in dic.items():
            
            if phrase_arr_clean_split[i][j]  in k[0]:
            
                Sum += int(k[1])
                check += 1 # Проверка на ввод некорректных символов
        
    #print(check)
    
    if check != len(phrase_arr_clean_split[i]):
        flag = 2
        break               
    
    phrase_arr_count.append(Sum)   

#print(phrase_arr_count)


for i in range(len(phrase_arr_count)-1):
    if phrase_arr_count[i] != phrase_arr_count[i + 1]:
        flag = 0
        
      
    
if flag == 1:
    print("Парам пам-пам")
elif flag == 0:
    print("Пам парам")
elif flag == 2:
    print("Error")
    

    
        