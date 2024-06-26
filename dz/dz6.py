"""Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума).
На вход подается список с элементамиlist_1 и границы диапазона в виде чисел min_number, max_number."""



def find_indexes(list_1, min_number, max_number):

        
 
    for i in range(len(list_1)):
        if min_number <= list_1[i] <= max_number:
            print(i)

# Пример использования
list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10
find_indexes(list_1, min_number, max_number)
'''Функция находит индексы элементов, значения которых принадлежат заданному диапазону.
            Args:
            list_1: Список.
            min_number: Минимальное значение.
            max_number: Максимальное значение.
            Returns:
            Список индексов.'''
'''-----------------------------------------------------'''
''' Заполните массив элементами арифметической прогрессии. 
Её первый элемент a1, разность d и количество элементов n будет задано автоматически. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.'''
def fill_array(a1, d, n):
  
    return [a1 + i * d for i in range(n)]


# Пример использования
a1 = 2
d = 3
n = 4
array = fill_array(a1, d, n)
print(array, sep='\n')