from random import randint
from art import logo

EASY_LEVEL_TURN=10
HARD_LEVEL_TURN=5

def comparison(u_guess,guess_no,turns):
    """checks answer against guess and returns the number of turns remaining """
    if u_guess > guess_no:
         print("TOO HIGH")
         return turns-1
    elif u_guess < guess_no:
         print("TOO LOW")
         return turns-1
    else:
        print(f"You Got it! The answer is {guess_no}")



def game_level():
    level = input("choose the difficulty, Type 'hard' or 'easy'").lower()
    if level == "hard":
        return HARD_LEVEL_TURN
    else:
        return EASY_LEVEL_TURN



def game():
    print(logo)
    print("Welcome To Number Guessing Game!")
    print("I'm thinking of a Number between 1 to 100.")
    answer= randint(1,100)

    turns=game_level()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        guess=int(input("Make the guess:"))
        turns = comparison(guess,answer,turns)
        if turns==0:
            print("You have run out of guesses, You loose!!")
            return
        elif guess != answer:
            print("Guess again:")


game()
