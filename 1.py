def multiples_of_3():
    numbers = set()
    for number in range(3, 1000, 3):
        numbers.add(number)
    return numbers

def multiples_of_5():
    numbers = set()
    for number in range(5, 1000, 5):
        numbers.add(number)
    return numbers



print(sum(multiples_of_3().union(multiples_of_5())))