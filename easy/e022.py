import string


def print_rangoli(size):
    if size > 26:
        size = size % 26
    alphas = list(string.ascii_lowercase[:size])
    rev_alphas = list(reversed(alphas))
    w = (size * 2) + (size - 1) * 2 - 1

    # Upper triangle construction
    for row in range(size):
        idx = alphas.index(rev_alphas[row])
        st_pattern = [rev_alphas[i] for i in range(row + 1)]
        rv_pattern = [alphas[i] for i in range(idx, size)][1:]
        pattern = "-".join(st_pattern + rv_pattern)
        print(pattern.center(w, "-"))

    # Lower triangle construction
    for row in range(size, 1, -1):
        idx = alphas.index(rev_alphas[row - 1])
        st_pattern = [rev_alphas[i] for i in range(row - 1)]
        rv_pattern = [alphas[i] for i in range(idx + 1, size)][1:]
        pattern = "-".join(st_pattern + rv_pattern)
        print(pattern.center(w, "-"))


if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)
