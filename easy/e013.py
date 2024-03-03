def swap_case(string: str) -> str:
    "This function converts all lowercase letters to uppercase letters and vice versa"
    cs_s = ""
    for char in string:
        if char.isupper():
            cs_s += char.lower()
        else:
            cs_s += char.upper()
    return cs_s


if __name__ == "__main__":
    s = input()
    result = swap_case(s)
    print(result)
