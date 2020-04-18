from random import choices
from collections import Counter
print('4 Урок 3 Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.')
print('функцию F заменим на element_iz_spiska.')
handle = open(r"D:\pytnon\text4.txt")# открываем файл по адресу в память
imena_str = handle.read() # читаем открытый файл , он преобразовывается в строку <class 'str'>
imena_list = imena_str.split() # читаем строку , она преобразовывается в список <class 'list'>
print(type(imena_list), imena_list)    # определяем тип переменной (это будет <class 'list'> ) и выводим список

def element_iz_spiska(N): # вводим функцию
    letters = []  # задаем пустой список
    for word in imena_list:  # для каждого имени (" word" это фунция в питоне) в имеющемся списке имен читаем первую букву и записываем её в заданный пустой список letters
        letters += word[0]
    print('Первые буквы имен в  том порядке. как были имена:', type(letters), letters)
    letters_dict = {}  # задаем пустой словарь
    for let in letters:  # для каждоЙ буквы ("let" это фунция в питоне) в имеющемся списке букв(letters) читаем каждую букву и записываем её в заданный пустой словарь (letters_dict)
        letters_dict[let] = letters.count(let)
    print('Подсчет количества букв и расположение их по первой подсчитанной букве:', type(letters_dict), letters_dict)
    list_d = []  # задаем пустой список
    list_d = list(letters_dict.items())  # СЛОВАРЬ превращаем в СПИСОК
    # СПИСОК сортируем по возрастанию, начиная с первой буквы
    list_d.sort(key=lambda i: i[1])  # сортируем по возрастанию
    print('Первые буквы отсортированные по возрастанию:', type(list_d), list_d)
    print(list_d[0:1])  # выводим первый элемент списка
    letters = list_d[0:1]
    print('Самая редкая буква:', type(letters), letters)  # выводим Самая редкая буква: <class 'list'> [('д', 1)]
    print(list_d[N])  # выводим заданный элемент списка ('д', 1)
    print("Самая редкая первая буква имени:", list_d[N][0])  # выводим заданный элемент списка просто буквой д

element_iz_spiska(0)