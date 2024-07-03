# Условная конструкция. Операторы if, elif, else

k,l,m = int(input()), int(input()), int(input())

if k==l==m:
    print(3)
elif k==l or k==m or l==m:
    print(2)
else:
    print(0)
