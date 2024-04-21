nums = []
for i in range(5):
    n = int(input("Введите число: "))
    nums.append(n)

nums = []
for i in range(5):
    nums.append(int(input("Введите число: ")))
    

nums = [int(input("Введите число: ")) for i in range(5)]

def create_arr(length):
    nums = [int(input("Введите число: ")) for i in range(length)]
    
create_arr(int(input("Введите длину: ")))



print(*[f"{i}-й пошел" for i in range(1,10)])