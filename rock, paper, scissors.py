# rock, paper, scissor game 
import random 

while True:
    print("\tRock, Paper, Scissors Game ")
    userInput = input("Choose your move : ")
    gameOptions = ["rock", "paper", "scissors"]
    computerInput = random.choice(gameOptions)

    # creating the conditions
    if  computerInput == userInput:
        print(f"Both selected {userInput}. It's a tie!")
    elif userInput == "rock":
        if computerInput == "paper":
            print("Paper covers rock! Computer Win.")
        else:
            print("Rock smashes scissors! You win.")
    elif userInput == "paper":
        if computerInput == "scissors":
            print("Scissors cut paper! Computer Win.") 
        else:
            print("Paper cover rock! You Win.")
    elif userInput == "scissors":
        if computerInput == "rock":
            print("Rock shames scissors! Computer Win.")
        else:
            print("Scissors cut paper! You Win.")

    # want to play again 
    play_again = input("Play again? (y / n): ")
    if play_again.lower() != "y":
        break


