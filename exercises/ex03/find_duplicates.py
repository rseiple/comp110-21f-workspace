"""Finding duplicate letters in a word."""

__author__ = "730524618"

i = 0   
word: str = str(input("Enter a word: "))
duplicate: bool = False

while i < len(word):
    j = i + 1
    char: str = str(word[i])
    while j < len(word):
        if word[j] == char:
            duplicate = True
        j = j + 1   
    i = i + 1
print(duplicate)


