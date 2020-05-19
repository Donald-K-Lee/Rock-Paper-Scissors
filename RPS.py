# Libraries
import random

# Options
r = "rock"
p = "paper"
s = "scissors"

def lost():
    print(opponent + " beats " + you)
    print("\nYou lose")
    chose()

def win():
    print(you + " beats " + opponent)
    print("\nYou win")
    chose()

def draw():
    print("You both chose " + you)
    print("\nDRAW")
    chose()

# Picks the opponent's weapon and decides the winner with if statements
def randomize():
    global you
    global opponent
    opponent = random.choice([r, p, s])
    print("You chose " + you)
    print("Your opponent chose " + opponent)
    if opponent == r and you == s:
        lost()
    elif opponent == s and you == p:
        lost()
    elif opponent == p and you == r:
        lost()
    elif opponent == you:
        draw()
    else:
        win()

def chose():
    global you
    you = input("Choose your weapon:").strip().capitalize()  # Here
    print("")
    if you == "R":
        you = r
        randomize()
    elif you == "S":
        you = s
        randomize()
    elif you == "P":
        you = p
        randomize()
    elif you == "Stop":
        print("Game ended")
    else:
        print("Please try again and type either, P, R, or S ")
        chose()

print("Type:\n P for Paper\n S for Scissors\n R for Rock\n \"Stop\" to end the game")
chose()