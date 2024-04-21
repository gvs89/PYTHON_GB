'''import random
def create_arr(length):
    nums = [random.randint(0, 99) for i in range(length)]
def count_elements(array):
    count = 0
    for i in range(1, len(array) - 1):
        if array[i] > array[i - 1] and array[i] > array[i + 1]:
            count += 1
    return count

# Пример использования

result = count_elements(create_arr(9))
print(result)'''


list1 = [1, 2, 3, 2, 1, 2]
def count_pairs(list1):
    count = 0
    for i in range(len(list1)):
        for j in range(i + 1, len(list1)):
            if list1[i] == list1[j]:
                count += 1
    return count

result = count_pairs(list1)
print(result)



def recursive(numbers):
    if len(numbers) <= 1:
        return 0
    first_num = numbers[0]
    rest_nums = numbers[1:]
    count = 0
    for i in rest_nums:
        if first_num == i:
            count += 1
    return count + recursive(rest_nums)