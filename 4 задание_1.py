import random
print('4 Урок 1 Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из первого списка (могут повторяться, можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию random);.')
handle = open(r"D:\pytnon\text4.txt")# открываем файл по адресу в память
imena_str = handle.read() # читаем открытый файл , он преобразовывается в строку <class 'str'>
imena_list = imena_str.split() # читаем строку , она преобразовывается в список <class 'list'>
print(type(imena_str), imena_str)  # проверяем строку <class 'str'>
print(type(imena_list), imena_list) # проверяем список <class 'list'>
N=100  # значение ставим
list_100 = random.choices(imena_list, k=N) # берем слова из imena_list , рассортируем их случайныс образом и записываем их в список list_100
print(type(list_100), list_100) # проверяем список list_100 <class 'list'> и выводим list_100
def rand_100(): # вводим функцию
    list_100_1 = random.choices(imena_list, k=N) # берем слова из imena_list , рассортируем их случайныс образом и записываем их в список list_100_1
    print(type(list_100_1), list_100_1) # проверяем список list_100_1 <class 'list'> и выводим list_100_1
rand_100() # вызываем функцию rand_100() без ввода переменной этой функции(она была определена ранее N=100)
def rand_8(N): # вводим функцию
    list_8_1 = random.choices(imena_list, k=N) # # берем слова из imena_list , рассортируем их случайныс образом и записываем их в список list_8_1
    print(type(list_8_1), list_8_1) # проверяем список list_8_1 <class 'list'> и выводим list_8_1
rand_8(8) # вызываем функцию rand_100() с вводом переменной этой функции(определяем ее N=8)


