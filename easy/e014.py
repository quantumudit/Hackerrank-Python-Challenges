def split_and_join(string):
    elements = string.split(" ")
    return "-".join(elements)


if __name__ == "__main__":
    line = input()
    result = split_and_join(line)
    print(result)
