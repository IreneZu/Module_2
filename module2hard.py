# Слишком древний шифр

left_num = int(input())

# Находим все числа, которым кратно left_num
factors = []
for i in range(3,left_num+1):
    if left_num % i == 0:
        factors += [i]

# Составляем пары
pairs = []
for i in range(1,(left_num-1)//2+1):
    for j in factors: # цикл по множителям
        if i < j/2:   # из пар [a, b] берем только a<b
            pairs += [i, j - i]

print(*pairs, sep='')