size = list(map(int, input().split()))
l = size[0]
w = size[1]
symbol = ".|."

# Creates the top pattern
for i in range(1, l, 2):
    pattern = symbol * i
    print(pattern.center(w, "-"))

# Writes the "WELCOME" text
print("WELCOME".center(w, "-"))

# Creates the bottom pattern
for i in range(2, l, 2):
    pattern = symbol * (l - i)
    print(pattern.center(w, "-"))
