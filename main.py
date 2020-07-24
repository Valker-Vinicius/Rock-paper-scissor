from random import choice
from facilitators import color

options = ('rock','paper','scissor')

while True:
    print(color.bolder())

    user_choice = " "
    machine = choice(options)
    player = str(input("Let's play rock, paper or scissor, so, make your choice: ")).strip().lower()
    
    if player not in options:
        print(color.red("please select a valid option"))
    
    else:
        print(f"As you choiced {color.blue(player)} and i choiced {color.blue(machine)}")

        
        if player == "rock" and machine == "paper":
            print(color.red("You lose..."))

        elif player == "paper" and machine == "scissor":
            print(color.red("You lose..."))

        elif player == "scissor" and machine == "rock":
            print(color.red("You lose..."))

        elif player == machine and machine == player:
            print(color.yellow("It's a draw!"))

        else:
            print(color.green("You win!"))

        while user_choice not in "NY":
            user_choice = str(input("Do you want to stay playing? [Y/N] ")).upper()

        if user_choice == "N":
            print('E X I T I N G...')
            break
