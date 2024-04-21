var1 = '5 4' 
var2 = '1 3 5 7 9' 
var3 = '2 3 4 5' 

n, m = map(int, var1.split())
first_set_str = var2
second_set_str = var3
first_set = list(map(int, first_set_str.split()))
second_set = list(map(int, second_set_str.split()))
common_elements = []
for num in first_set:
    if num in second_set and num not in common_elements:
        common_elements.append(num)
common_elements.sort()
print(*common_elements) 