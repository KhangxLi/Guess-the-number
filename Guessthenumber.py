import random
import sys
def gameplay():
    '''Guess the number game'''
    number = random.randint(1, 1001)
    guesses = 0
    print("Guess our whole number between 1 and 1000\n")
    while True:
        try:
            player_guess = int(input("Enter your guess here:"))
            if player_guess == number:
                print("\nCorrect! You win!")
                guesses = guesses + 1
                break
            elif player_guess > number:
                print("\nWrong! The answer is lower than that.")
                guesses = guesses + 1
            elif player_guess < number:
                print("\nWrong! The answer is higher than that.")
                guesses = guesses + 1
        except ValueError:
            print("\nThat's not a whole number, try again.")
            continue
    print('You got it in', guesses, 'guesses!\n')

gameplay()
playagain = str(input("Play again? (yes or no)\n"))
if playagain == 'yes':
    gameplay()
else:
    sys.exit
