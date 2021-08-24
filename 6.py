total = 0

for num in range(1, 101):
    total += num * num

total2 = 0

for num in range(1, 101):
    total2 += num

print((total2 * total2) - total)

# Homework: rewrite in under 4 lines
# 2 useful tools:
    # Sum function
        # sum([1, 2, 3]) => 1 + 2 + 3 = 6
    # List comprehensions
        # [n * 2 for n in range(10)] => [0, 2, 4, 6, ..., 20]