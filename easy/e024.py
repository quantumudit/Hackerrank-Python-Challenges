from itertools import product

a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

a_b = product(a, b)

print(*a_b)
