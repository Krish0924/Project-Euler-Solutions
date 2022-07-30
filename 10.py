primeNumbers = [False, False] + [True] * 1_999_999 # Change to actually be 2000000 long
#                 0      1     2 .... 2,000,000
numbers = []
# Go to the next true (for loop that checks if that index is true)
# change all the multiples of that index to false (for loop hint: use start, stop, step)

for num in range(2, 2_000_001):# every num upto 2,000,000
    if primeNumbers[num]: # if num is prime
        for i in range(num * 2, 2_000_001, num):# every multiple of num up to 2,000,000
            primeNumbers[i] = False

# All the primes below 2,000,000 are whatever indicies are true
for num2 in range(2, 2_000_001):
    if primeNumbers[num2]:
        numbers.append(num2)

print(sum(numbers))