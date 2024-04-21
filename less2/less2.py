#Списки
list_1 = [] # Создание пустого списка
list_2 = list() # Создание пустого списка
list_1 = [7, 9, 11, 13, 15, 17]
print(*list_1)
################################################################
list_1 = [7, 9, 11, 13, 15, 17]
print(list_1[0]) # 7

################################################################
list_1 = [7, 9, 11, 13, 15, 17]
print(len(list_1)) # 6

################################################################
list_1 = list() # создание пустого списка
for i in range(5): # цикл выполнится 5 раз
    n = int(input()) # пользователь вводит целое число
    list_1.append(n) # сохранение элемента в конец списка
# 1-я итерация цикла(повторение 1): n = 12, list_1 = [12]
# 2-я итерация цикла(повторение 2): n = 7, list_1 = [12, 7]
# 3-я итерация цикла(повторение 3): n = -1, list_1 = [12, 7, -1]
# 4-я итерация цикла(повторение 4): n = 21, list_1 = [12, 7, -1, 21]
# 5-я итерация цикла(повторение 5): n = 0, list_1 = [12, 7, -1, 21, 0]
print(list_1) # [12, 7, -1, 21, 0]
#################################################################
list_1 = [12, 7, -1, 21, 0]
print(list_1.pop()) # 0
print(list_1) # [12, 7, -1, 21]
print(list_1.pop()) # 21
print(list_1) # [12, 7, -1]
print(list_1.pop()) # -1
print(list_1) # [12, 7]
################################################################
"""Удаление конкретного элемента из списка.
Надо указать значение индекса в качестве аргумента функции pop:"""
list_1 = [12, 7, -1, 21, 0]
print(list_1.pop(0)) # 12
print(list_1) # [7, -1, 21, 0]
#####################################################################
#Добавление элемента на нужную позицию.
#Функция insert — указание индекса (позиции) и значения.
list_1 = [12, 7, -1, 21, 0]
print(list_1.insert(2, 11))
print(list_1) # [12, 7, 11, -1, 21, 0]
####################################################################
#Срез списка
###● Отрицательное число в индексе — счёт с конца списка
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[0]) # 1
print(list_1[1]) # 2
print(list_1[len(list_1)-1]) # 10
print(list_1[-5]) # 6
print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[:2]) # [1, 2]
print(list_1[len(list_1)-2:]) #[9, 10]
print(list_1[2:9]) # [3, 4, 5, 6, 7, 8, 9]
print(list_1[6:-18]) # []
print(list_1[0:len(list_1):6]) # [1, 7]
print(list_1[::6]) # [1, 7]


'''Кортеж — это неизменяемый список.
Тогда для чего нужны кортежи, если их нельзя изменить? В случае защиты
каких-либо данных от изменений (намеренных или случайных). Кортеж занимает
меньше места в памяти и работают быстрее, по сравнению со списками'''
t = () # создание пустого кортежа
print(type(t)) # class <'tuple'>
t = (1,)
print(type(t))
t = (1)
print(type(t))
t = (28, 9, 1990)
print(type(t))
colors = ['red', 'green', 'blue']
print(colors) # ['red', 'green', 'blue']
t = tuple(colors)
print(t) # ('red', 'green', 'blue')
t = tuple(['red', 'green', 'blue'])
print(t[0]) # red
print(t[2]) # blue
for e in t:
    print(e) # red green blue
    t[0] = 'black' # TypeError: 'tuple' object does not support(нельзя изменять кортеж)


'''Словари — неупорядоченные коллекции произвольных объектов с
доступом по ключу.
В списках в качестве ключа используется индекс элемента. В словаре для
определения элемента используется значение ключа (строка, число).'''
dictionary = {}
dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ←
# типы ключей могут отличаться
print(dictionary['up']) # ↑
# типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента
for item in dictionary: # for (k,v) in dictionary.items():
    print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# down: ↓
# right: →

'''Множества содержат в себе уникальные элементы, не обязательно
упорядоченные.
Одно множество может содержать значения любых типов. Если у Вас есть два
множества, Вы можете совершать над ними любые стандартные операции,
например, объединение, пересечение и разность. Давайте разберем их.'''
colors = {'red', 'green', 'blue'}
print(colors) # {'red', 'green', 'blue'}
colors.add('red')
print(colors) # {'red', 'green', 'blue'}
colors.add('gray')
print(colors) # {'red', 'green', 'blue','gray'}
colors.remove('red')
print(colors) # {'green', 'blue','gray'}
colors.remove('red') # KeyError: 'red'
colors.discard('red') # ok
print(colors) # {'green', 'blue','gray'}
colors.clear() # { }
print(colors) # set()

'''Операции со множествами в Python'''
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1, 2, 3, 5, 8, 13,
i = a.intersection(b) # i = {8, 2, 5}
dl = a.difference(b) # dl = {1, 3}
dr = b.difference(a) # dr = {13, 21}
q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}
'''Неизменяемое или замороженное множество(frozenset) — множество, с которым
не будут работать методы удаления и добавления.'''
a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b) # frozenset({1, 2, 3, 5, 8})
################################
'''List Comprehension
У каждого языка программирования есть свои особенности и преимущества. Одна
из культовых фишек Python — list comprehension (редко переводится на русский, но
можно использовать определение «генератора списка»). Comprehension легко
читать, и их используют как начинающие, так и опытные разработчики.
List comprehension — это упрощенный подход к созданию списка, который
задействует цикл for, а также инструкции if-else для определения того, что в итоге
окажется в финальном списке.
1. Простая ситуация — список:'''
list_1 = [i for item in range(5)]
'''2. Выборка по заданному условию:'''
list_1 = [i * 2 for i in range(10) if i % 2 == 0]