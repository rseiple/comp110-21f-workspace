"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730524618"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
rand: int = int(randint(1, 100)) 
print("Your fortune cookie says... ")
if rand > 75:
    print("Bad luck is in your future.")
else:
    if rand > 50:
        print("You will perform well in your next test, whatever it may be.")
    else:
        if rand > 25:
            print("A drastic change will visit you soon.")
        else:
            if rand > 0:
                print("You will be paid a visit by an old friend.")
print("Now, go spread positive vibes!")