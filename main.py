
import random

# words, with no newlines
words = list(map(lambda word: word.strip(), open("words.txt", "r").readlines()))

# A set can check if a word is part of it
# in O(1) time, as opposed to something like
# a O(n) linear search.
dictionary = set(words)

def valid_guess(guess: str) -> bool:
    return guess.lower() in dictionary

def get_guess() -> str:
    x = input("Enter a 5 letter word: ")
    while not valid_guess(x):
        print("invalid guess!")
        x = input(f"Enter a {LENGTH} letter word: ")
    return x

# chosen for my terminal
GREEN_SQUARE  = "✓"
YELLOW_SQUARE = "-"
GREY_SQUARE   = " "

LENGTH = 5
# java is quivering right now
#  ANSWER = random.choice(words)
ANSWER = "light"

def new_game():
    ANSWER = random.choice(words)

def print_squares(original_guess: str):
    guess = list(original_guess)
    result = [GREY_SQUARE for _ in range(LENGTH)]

    for idx, char in enumerate(ANSWER):
        if char == guess[idx]:
            result[idx] = GREEN_SQUARE
            guess[idx] = None
        elif char in guess:
            # remove the first instance of the char
            guess_index = guess.index(char)
            result[guess_index] = YELLOW_SQUARE
            guess[guess_index] = None

    print(f"|{''.join(result)}|")
    print(f"|{original_guess}|")
    print("")

def evaluate_guess(guess: str) -> bool:
    """ returns True if the guess was correct """

    return False

# use `main` so that this file
# can be properly imported as a module
def main():
    print(f"{ANSWER=}")
    print_squares("kitty")
    print_squares("start")
    print_squares("brown")
    print_squares("limit")
    print_squares("light")

if __name__ == "__main__":
    main()

