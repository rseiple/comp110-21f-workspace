"""An exercise in remainders and boolean logic."""

__author__ = "ENTER YOUR 9-DIGIT PID HERE"


# Begin your solution here...
i: int = int(input("Enter an int: "))

if i % 2 == 0:
    if i % 7 == 0:
        print("TAR HEELS")
    else:
        print("TAR")
else:
    if i % 7 == 0:
        print("HEELS")
    else:
        print("CAROLINA")