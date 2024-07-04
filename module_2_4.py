# Цикл for. Элементы списка. Полезные функции в цикле

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
numbers.sort()
if numbers.count(1) > 0:
    numbers.remove(1)  # единица не нужна

primes = []
not_primes = []
for i in range(len(numbers)):
    is_prime = True
    for j in range(i):
        if numbers[i] % numbers[j] == 0:
            not_primes.append(numbers[i])
            is_prime = False
            break
    if is_prime:
        primes.append(numbers[i])

print('Primes:', primes)
print('Not Primes:', not_primes)