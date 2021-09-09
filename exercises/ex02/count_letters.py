"""Counting letters in a string."""

__author__ = "730524618"


# Begin your solution here...
letter: str = str(input("What letter do you want to search for? "))
word: str = str(input("Enter a word: "))
wordlen: int = len(word)
i: int = 0
lettercount: int = 0
while i < wordlen:
    if (word[i]) == letter:
        lettercount = lettercount + 1
    i = i + 1
print("Count: " + str(lettercount))
