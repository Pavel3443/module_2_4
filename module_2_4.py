numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for a in numbers:
    is_prime = True
    if a > 1:
        for b in range(2, a):
            if a % b == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(a)
        else:
            not_primes.append(a)


print('Primes: ', primes)
print('not_primes: ', not_primes)

