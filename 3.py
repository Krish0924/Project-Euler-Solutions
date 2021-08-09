import tqdm
def is_prime(number):
    for factor in range(2, number // 2 + 1):
        if number % factor == 0:
            return False
    return True

n = 600851475143

x = 2

while True:
    x += 1
    if n % x == 0:
        p = n // x
        if is_prime(p):
            print(p)
            break
    
        

print(is_prime(3)) # should be True
print(is_prime(4)) # should be False

# find all factors of 600,851,475,143
    # take advantage of the fact that when you find one factor of n, n / factor is another factor
    # first time that n / factor is a prime, that's the biggest
# go backwards (biggest to smallest) and find the first prime one

# n := 600851475143
# x starts at 1
# loop forever:
    # is x a factor of n?
    # if so,
        # p = n / x, p is another factor of n
        # if p is prime, that's the biggest primme factor
    # increment x by one