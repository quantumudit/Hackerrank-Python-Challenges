def minion_game(string: str) -> str:
    vowels = ["a", "e", "i", "o", "u"]
    string = string.lower()

    stuart_score = 0
    kevin_score = 0

    for i, char in enumerate(string):
        if char in vowels:
            kevin_score += len(string) - i
        else:
            stuart_score += len(string) - i

    if stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    elif stuart_score < kevin_score:
        print(f"Kevin {kevin_score}")
    else:
        print("Draw")


if __name__ == "__main__":
    s = input()
    minion_game(s)
