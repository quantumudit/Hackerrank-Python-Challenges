from itertools import permutations

s, k = input().split()

perms = sorted(["".join(val) for val in permutations(s, int(k))])

for val in perms:
    print(val)
