import modul1 # импорт способ №1

print(modul1.max1(5, 9))

from modul1 import max1 # импорт способ №2

print(max1(10, 9))

from modul1 import * # импорт всех функций

print(max1(10, 49))

import modul1 as m1 # импорт с переименовыванием модуля

print(m1(10, 9))