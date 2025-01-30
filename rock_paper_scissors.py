
import random
running=True
options=('rock','paper','scissors')
computer = random.choice(options)

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("enter your choice (rock, paper or scissors)")

    print(f"player: {player}")
    print(f"computer: {computer}\n")

    if player==computer:
        print("Its'a Tie")
    elif player=='rock' and computer=='paper':
        print("You Lose")
    elif player=='paper' and computer=='scissors':
        print("You Lose")
    elif player=='scissors' and computer=='rock':
        print("You Lose")
    else:
        print("You Win")

    again=input("To play again press (y/n)").lower()
    if not again=='y':
        running=False
print("\n---------Thanks for playing--------")
