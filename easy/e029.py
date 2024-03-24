grp_a_size, grp_b_size = map(int, input().split())
grp_a = [input() for _ in range(grp_a_size)]
grp_b = [input() for _ in range(grp_b_size)]

for n in grp_b:
    if n in grp_a:
        idxs = [str(idx + 1) for idx, m in enumerate(grp_a) if m == n]
        print(" ".join(idxs))
    else:
        print(-1)
