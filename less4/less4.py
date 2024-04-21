def f(x):
    return x ** 2
print(f(2))
''' 1. В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар
(число; квадрат числа).
Пример: 1 2 3 5 8 15 23 38
Получить: [(2, 4), (8, 64), (38, 1444)]'''

data = [1, 2, 3, 5, 8, 15, 23, 38]
out = []
for i in data :
    if i % 2 == 0:
        out.append((i, i ** 2))
print(out)
''' Решение с помощью lambda'''

def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
res = where(lambda x: x % 2 == 0, res)
print(res) # [2, 8, 38]
res = list(select(lambda x: (x, x ** 2), res))
print(res)

'''2. Использование функции map.Результат работы map() — это итератор. По итератору можно пробежаться только один раз. Чтобы работать несколько раз с одними данными, нужно сохранить данные (например, в виде списка).'''
def where(f, col):
    return [x for x in col if f(x)]
data = '1 2 3 5 8 15 23 38'.split()
res = map(int, data)
res = where(lambda x: x % 2 == 0, res)
res = list(map(lambda x: (x, x ** 2), res))
print(res)

'''3. Функция filter применяет указанную функцию к каждому элементу итерируемого объекта и
возвращает итератор с теми объектами, для которых функция вернула True. '''
data = [x for x in range(10)]
res = list(filter(lambda x: x % 2 == 0, data))
print(res) # [0, 2, 4, 6, 8]

'''Функция zip
Функция zip() применяется к набору итерируемых объектов и возвращает итератор с кортежами
из элементов входных данных
На выходе получаем набор данных, состоящий из элементов соответствующих
исходному набору.'''
users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]
data = list(zip(users, ids, salary))
print(data) # [('user1', 4, 111), ('user2', 5, 222), ('user3', 333)]

'''Функция enumerate() применяется к итерируемому объекту и возвращает новый итератор с
кортежами из индекса и элементов входных данных.
Функция enumerate() позволяет пронумеровать набор данных.'''

users = ['user1', 'user2', 'user3']
data = list(enumerate(users))
print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3))]