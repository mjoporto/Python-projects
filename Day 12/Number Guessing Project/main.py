from random import randint
import art

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
turns = 0

#Function to set difficulty.
def set_difficulty():
    level = input('choose a difficulty.  Type "easy" or "hard": ')
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


#Function to check users' guess against actual number.
def check_answer(user_guess, actual_answer, turns):
#check guess and return number of turns left
    if user_guess > actual_answer:
        print("Too High")
        return turns -1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns -1
    else:
        print(f"You got it!  The answer was {actual_answer}")


def game():
    #Choosing a random number between 1 and 100.
    print(logo)
    print("Welcome to the guessing game!")
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1,100)
    #print(f"Psst, the correct answer is {answer}")

    turns = set_difficulty()
    print(f"You have {turns} attempts remaining to guess the number.")

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        #Let the user guess a number.
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose")
            return
        elif guess != answer:
            print("Guess again!")

game()

#Track the number of turns and reduce by 1 if they get it wrong.



#Repeat the guessing functionality if they get it wrong.