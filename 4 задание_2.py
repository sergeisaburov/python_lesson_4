import random
print('4 Урок 2 Напишите функцию вывода самого частого имени из списка на выходе функции F.')
handle = open(r"D:\pytnon\text4.txt")# открываем файл по адресу в память
imena_str = handle.read() # читаем открытый файл , он преобразовывается в строку <class 'str'>
imena_list = imena_str.split() # читаем строку , она преобразовывается в список <class 'list'>
def rand_8(N): # вводим функцию
    list_8_1 = random.choices(imena_list, k=N) # # берем слова из imena_list , рассортируем их случайныс образом и записываем их в список list_8_1
    print(type(list_8_1), list_8_1) # проверяем список list_8_1 <class 'list'> и выводим list_8_1
    list_8_1.sort(key=lambda i: i[1], reverse=True)  # сортируем по убыванию
    print(list_8_1)
    print(list_8_1[0:1])  # выводим первый элемент списка
rand_8(100) # вызываем функцию rand_100() с вводом переменной этой функции(определяем ее N=8)