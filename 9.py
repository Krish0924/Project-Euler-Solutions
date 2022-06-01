def tripleChecker(a, b, c):
    if a * a + b * b == c * c:
        if a + b + c == 1000:
            return True
    return False

for a in range(1, 334):
    for b in range(a, 500):
        c = 1000 - a - b
        if tripleChecker(a, b, c):
            print(a * b * c)