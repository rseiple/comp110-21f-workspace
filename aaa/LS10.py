"""Challenge Question #1"""

choice: int = int(input("Enter a number: "))

if choice < 50:
    if choice < 25:
        print("A")
    else:
        print("B")
if choice > 50:
    if choice < 75:
        print("C")
    else:
        print("D")