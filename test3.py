import primer

n = int(input('Введите число простых чисел, сумма которых будет подсчитана: '))
primes = primer.primes(n)
print('Сумма всех простых чисел:')
print(f'{" + ".join(str(i) for i in primes)} = {sum(primes)}')
