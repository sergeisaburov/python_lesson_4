from random import choices
from collections import Counter
name_list = ['Alexandra', 'Bella', 'Violleta', 'Gabriella', 'Cornelius', 'Stephany', 'Oliver',
             'Robert', 'Feliciti', 'Chloe', 'Charlotte', 'Tara', 'Steven', 'Mia', 'Ophelia', 'John',
             'Isabella', 'Ethan', 'Elaine', 'Jennifer']
# 3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.
def element_iz_spiska(N): # вводим функцию
    letters = []  # задаем пустой список
    for word in name_list:  # для каждого имени (" word" это фунция в питоне) в имеющемся списке имен читаем первую букву и записываем её в заданный пустой список letters
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
    print(list_d[N])  # выводим заданный элемент списка
element_iz_spiska(0)

