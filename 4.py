def pal(num):
    # num = 1234
    # str(num) = "1234"
    # str(num)[::-1] = "4321"
    if str(num)[::-1] == str(num):
        return True
    else:
        return False

assert not pal(1234)
assert pal(9009)

# find biggest product of 2 3 digit nums that is a palindrome

isPal = []

for threeDigit in range(100, 1000):
    for threeDigit2 in range(100, 1000):
        if pal(threeDigit * threeDigit2):
            isPal.append(threeDigit * threeDigit2)

print(max(isPal))

print(max(x for a in range(100, 1000) for b in range(100, 1000) if str(x := a * b) == str(x)[::-1]))