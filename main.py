# Rock, Paper, Scissors Game
from random import randint

rock = "R"
paper = "P"
scissors = "S"
#moves for the player
moves = ["R", "P", "S"]

while True:
    computer = moves[randint(0,2)]
    player = input("R, P or S? (or end the game)").upper()
    #If player decide to end the game
    if player == "end the game":
        print("The game has ended.")
        break
    # Tie between computer and player
    elif player == computer:
        print("Tie!")
        # Rock against scissors
    elif player == "S":
        if computer == "R":
            print("You lose!", computer, "beats", player)
        else:
            print("You win!", player, "beats", computer)
        # Paper against Rock
    elif player == "R":
        if computer == "P":
            print("You lose!", computer, "beats", player)
        else:
            print("You win!", player, "beats", computer)
    # Scissors against paper
    elif player == "S":
        if computer == "P":
            print("You lose!", computer, "beats", player)
        else:
            print("You win!", player, "beats", computer)
    else:
        print("Check your spelling...")
    
        





