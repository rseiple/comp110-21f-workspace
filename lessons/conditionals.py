"""An example of conditional (if-else) statements."""

SECRET: int = 3

print("I'm thinking of a number between one and five - what is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("You guessed correctly!")
    print("Have a wonderful day.")
else:
    print("aaaaaaaaaaaaaaaaaaaaaa")
    if guess > SECRET:
        print("Too high my guy.")
    else:
        print("Too low my guy.")

print("Game over.")