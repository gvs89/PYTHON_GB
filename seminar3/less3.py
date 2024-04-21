
string = "a a a b c a a d c d d"
seen = {}  
res = [] 
for i in string.split():
    if i not in seen:
        seen[i] = 0
        res.append(i)
    else:
        seen[i] += 1
        res.append(f"{i}_{seen[i]}")
print(" ".join(res))


text = str ("She sells sea shells on the sea ")

words = text.split()
words_c = set(words)
print(len(words_c))

n = input("fgfg")
max_value = 0
for num in n:
    if num == 0:
      break
    if num > max_value:
      max_value = num
print(max_value) 