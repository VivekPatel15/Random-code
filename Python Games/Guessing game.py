import random

wins = 0
number = 0
play = "y"

while play:
    print ("Randomizing number...")
    number = random.randint(1, 10)
    guess_input = input("Guess the number between 1-10: ")
    guess = int(guess_input)
    if guess == number:
        wins = wins + 1
        print ("Winner! You've guessed correctly {} times!".format(wins))
    else:
        print ("Sorry, incorrect.")

    play = "y" in input("Play again? Press y: ")
