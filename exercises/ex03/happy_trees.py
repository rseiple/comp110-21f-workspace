"""Drawing forests in a loop."""

__author__ = "730524618"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
repeatnum: int = int(input("Depth: "))
counter: int = 0
i = 1

if repeatnum > 0:
    while counter < repeatnum:
        print(TREE * i)
        i = i + 1
        counter = counter + 1
