"""Repeating a beat in a loop."""

__author__ = "730524618"


# Begin your solution here...
repeat: str = input("What beat do you want to repeat? ")
repeatnum: int = int(input("How many times do you want to repeat it? "))
counter: int = 0

if repeatnum > 0:
    while counter < repeatnum:
        output: str = (repeat + " ") * repeatnum
        counter = counter + 1
    output: len(output) - len(" ")
    print(str(output) + "h")
else:
    print("No beat...")