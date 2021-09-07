def is_prime(number):
    for factor in range(2, number // 2 + 1):
        if number % factor == 0:
            return False
    return True

primeNumbers = [2]

num = 1

while len(primeNumbers) < 10_001:
    num += 2
    if is_prime(num):
        primeNumbers.append(num)
        print(len(primeNumbers))
print(primeNumbers)