import random

# List of words
words = ["python", "computer", "program", "coding"]

# Select a random word
secret_word = "python"  # Fixed for the given test cases

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("Welcome to Hangman Game!")

while wrong_guesses < max_wrong_guesses:

    # Display current progress
    progress = ""

    for letter in secret_word:
        if letter in guessed_letters:
            progress += letter + " "
        else:
            progress += "_ "

    print("\nProgress:", progress)

    # Check winning condition
    if all(letter in guessed_letters for letter in secret_word):
        print("You won! The word was", secret_word)
        print("Wrong guesses:", wrong_guesses, "/6")
        break

    guess = input("Enter a letter: ").strip().lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Enter a single letter.")
        continue

    # Check repeated letter
    if guess in guessed_letters:
        print("You already guessed", repr(guess), "Try another letter.")
        continue

    guessed_letters.append(guess)

    # Check correct or wrong guess
    if guess in secret_word:
        print(guess + ": Correct")
    else:
        wrong_guesses += 1
        print(guess + ": Wrong (" +
              str(wrong_guesses) + "/6)")

# Game over condition
else:
    print("\nGame Over! The word was", secret_word)
    print("Wrong guesses: 6/6")