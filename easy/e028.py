def average(array):
    dist_hgts = set(array)
    return round(sum(dist_hgts) / len(dist_hgts), 3)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
