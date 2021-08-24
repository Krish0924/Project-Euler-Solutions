def isDivisible(possible):
    
    for i in range(1, 21):
        if possible % i > 0:
            return False
    return True
    
counter = 2520

while isDivisible(counter) == False:
   counter += 10

print(counter)