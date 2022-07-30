# nth triangular number is the sum of the first n natural numbers (triangular(4) = 1 + 2 + 3 + 4)
# generate those ^
# Find all the factors of each of them
# Whenever the number of factors is > 500, that's the answer!
# √n = n ^ 1/2

from math import floor

def factors(num):
    countOfFactors = 0
    for potentialFactor in range(1, floor(num ** 0.5 + 1)):
        if num % potentialFactor == 0:
            countOfFactors += 2
        if potentialFactor * potentialFactor == num:
            countOfFactors -= 1
    return countOfFactors

def triangularNumsW500factors():
    currentTriangular = 1
    addThingy = 2
    while factors(currentTriangular) <= 500:
        #make triangular numbers
        currentTriangular += addThingy
        addThingy += 1
    return currentTriangular

print(triangularNumsW500factors())