# Marc Galvez
# Project: Guessing Game
# September 3, 2023


def main():
    # Prompts users for input
    numberToGuess = float(input("Player 1 enter a number between 1 and 100: "))

    # Counts number of guesses
    guessCounter = 0

    # Verifies that the number entered is within parameters.
    while numberToGuess < 1 or numberToGuess > 100:
        print("The number that needs to be guessed should be between 1 and 100")
        numberToGuess = float(input("Player 1 enter a number between 1 and 100: "))
    else:
        guess = float(input("Enter a guess: "))
        GuessChecker(numberToGuess, guess, guessCounter)


def GuessChecker(
    numberToGuess, guess, guessCounter
):  # Function is used for readability.
    # Keeps the game going until the correct number is guessed
    while numberToGuess > 1 or numberToGuess < 100:
        guessCounter += 1  # Increments number of guesses
        # Tells user if guess is too high or too low
        if guess > numberToGuess:
            print("Too high")
        if guess < numberToGuess:
            print("Too low")
        if guess == numberToGuess:
            print(
                "You have reached the end. You made " + str(guessCounter) + " guesses."
            )
            break
        guess = float(input("Enter another guess: "))


main()
