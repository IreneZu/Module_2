# Условная конструкция. Операторы if, elif, else

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

i = -1
while i < len(my_list) - 1:
    i += 1
    if my_list[i] == 0:
        continue
    elif my_list[i] < 0:
        break
    else:
        print(my_list[i])
