list_1 = [1, 2, 3, 4, 5]
k = 6

# Введите ваше решение ниже


min_diff = float('inf')
closest_element = None
for element in list_1:
    diff = abs(element - k)
    if diff < min_diff:
        min_diff = diff
        closest_element = element
print(closest_element)