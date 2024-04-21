import random

def differense(a, b):
    
    list_1 = list()
    list_2 = list()
    list_3 = list()
    for i in range (0, a):
        number = random.randint(1, 5)
        list_1.append(number)
        print(list_1)
    for i in range (0, b):
        number = random.randint(1, 5)
        list_2.append(number)
        print(list_2)
    for i in range (len(list_1)):
        for j in range (len(list_2)):
            if list_1[i] != list_2[j]:
                list_3.append(list_1[i])
        print(list_3)

print(differense(6, 7))