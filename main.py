# A wordle clone, inspired by:
# https://github.com/SamKiehl/ButterDog-Bot/blob/master/main.py
#
# This has been tested with Python 3.10

import random

# A list of words with no newlines that the player
# might be asked to guess.
COMMON_WORDS = open("common-words.txt").read().splitlines()

# This is the dictionary the player's input will be
# tested against.
#
# Note: A set can check if a word is part of it
# in O(1) time, as opposed to something like
# a O(n) linear search for a list.
DICTIONARY = set(open("all-words.txt").read().splitlines())

# chosen for my terminal
GREEN_SQUARE  = "✓"
YELLOW_SQUARE = "-"
GREY_SQUARE   = " "

LENGTH = 5
GUESS_LIMIT = 6

# java is quivering right now
ANSWER = random.choice(COMMON_WORDS)

def valid_guess(guess: str) -> bool:
    return guess.lower() in DICTIONARY

def get_guess() -> str:
    x = input(f"Enter a {LENGTH} letter word: ")
    while not valid_guess(x):
        print("Invalid guess!")
        x = input(f"Enter a {LENGTH} letter word: ")
    return x.lower()

def print_squares(original_guess: str, guesses: int):
    result = [GREY_SQUARE for _ in range(LENGTH)]
    guess = list(original_guess) # we will delete letters, as to not find them more than once

    # mark all the letters in the correct place
    for index, char in enumerate(guess):
        if char == ANSWER[index]:
            result[index] = GREEN_SQUARE
            guess[index] = None

    # mark all the letters in the wrong place
    for char in ANSWER:
        if char in guess:
            guess_index = guess.index(char)
            if guess[guess_index] is not None:
                result[guess_index] = YELLOW_SQUARE
                guess[guess_index] = None

    print(f" {guesses + 1}/{GUESS_LIMIT} |{''.join(result)}|")
    print(f"     |{original_guess}|")
    print("")

def play_game():
    guesses = 0
    while (guess := get_guess()) != ANSWER and guesses < GUESS_LIMIT - 1:
        print_squares(guess, guesses)
        guesses += 1
    print_squares(guess, guesses)

    if guess == ANSWER:
        print("Good Job!")
    else:
        print(f'The word was "{ANSWER}"')

# use `main` so that this file
# can be properly imported as a module
def main():
    play_game()

if __name__ == "__main__":
    main()

