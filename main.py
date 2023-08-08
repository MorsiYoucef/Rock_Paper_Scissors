import random


x = str(input("(r) for rock,(p) for paper, (s) for scissors !"))

def game(x):
    computer = ["rock", "paper", "scissors"]
    random_computer = random.choice(computer)
    print("the computer choose :",random_computer)
    if x=='r' and random_computer== 'rock':

        print("equality!")
    if x == 'r' and random_computer == 'paper':
        print("you lose!")
    if x == 'r' and random_computer == 'scissors':
        print("you win")
    if x == 'p' and random_computer == 'paper':
        print("equality!")
    if x == 'p' and random_computer == 'rock':
        print("you win")
    if x == 'p' and random_computer == 'scissors':
        print("you lose")
    if x == 's' and random_computer == 'paper':
        print("you win")
    if x == 's' and random_computer == 'scissors':
        print("equality!")
    if x == 's' and random_computer == 'rock':
        print("you lose")
    s=str(input("do you want to play again?(y/n)"))
    if s == 'y':
        game(x = str(input("(r) for rock,(p) for paper, (s) for scissors !")))

game(x)
