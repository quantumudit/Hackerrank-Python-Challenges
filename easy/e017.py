def count_substring(string, sub_string):
    idx = 0
    count = 0
    while True:
        find_idx = string.find(sub_string, idx)
        if find_idx != -1:
            count += 1
            idx = find_idx + 1
        else:
            break
    return count


if __name__ == "__main__":
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
