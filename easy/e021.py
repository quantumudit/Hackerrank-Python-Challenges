def print_formatted(number):
    w = len(bin(number)[2:])
    for i in range(1, number + 1):
        decimal_num = str(i).rjust(w)
        octal_num = oct(i)[2:].rjust(w)
        hexadecimal_num = hex(i)[2:].upper().rjust(w)
        binary_num = bin(i)[2:].rjust(w)

        print(f"{decimal_num} {octal_num} {hexadecimal_num} {binary_num}")


if __name__ == "__main__":
    n = int(input())
    print_formatted(n)
