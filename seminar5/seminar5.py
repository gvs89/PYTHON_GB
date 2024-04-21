'''Последовательностью Фибоначчи называется последовательность чисел a0 , a1 , ..., an , ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). Требуется найти N-е число Фибоначчи Input: 7 Output: 21
Задание необходимо решать через рекурсию'''

def fibonacci(n):
  
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

# Пример использования
n = 7
fib_number = fibonacci(n)
print(fib_number)

def replace_grades(grades):
 
    min_grade = min(grades)
    max_grade = max(grades)
    for i in range(len(grades)):
        if grades[i] == min_grade:
            grades[i] = max_grade
        elif grades[i] == max_grade:
            grades[i] = min_grade
    return grades

# Пример использования
grades = [1, 3, 3, 3, 4]
new_grades = replace_grades(grades)
print(*new_grades)