values = ['1', '23', '42', 'asdfg']
transformation= lambda x:x
transformed_values = list(map(transformation, values))
if values == transformed_values:
 print('ok')
else:
 print('fail')

import math

orbits = [(1, 3), (2.5, 10), (10, 10), (6, 6), (4, 3)]

def find_farthest_orbit(list_of_orbits):
   
    elliptic_orbits = list(filter(lambda orbit: orbit[0] != orbit[1], list_of_orbits)) 
    areas = [math.pi * a * b for a, b in elliptic_orbits] 
    max_index = areas.index(max(areas))  
    return elliptic_orbits[max_index]


farthest_orbit = find_farthest_orbit(orbits)

print(*farthest_orbit)

'''Напишите функцию same_by(characteristic, objects), которая
проверяет, все ли объекты имеют одинаковое значение
некоторой характеристики, и возвращают True, если это так.
Если значение характеристики для разных объектов
отличается - то False. Для пустого набора объектов, функция
должна возвращать True. Аргумент characteristic - это
функция, которая принимает объект и вычисляет его
характеристику.
'''

def same_by(characteristic, objects):
    first = next(iter(objects), None)
    return all(characteristic(obj) == characteristic(first) for obj in objects)

values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
