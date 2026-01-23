# Define the choices array
choices = ["Rock", "Paper", "Scissors"]

# Get player input
playerChoice = input("Enter your choice (1=Rock, 2=Paper, 3=Scissors): ")

# Convert to integer
playerChoice = int(playerChoice)

# Error handling for player choice
if playerChoice < 1 or playerChoice > 3:
    print("Error: Choice must be between 1 and 3.")
else:
    # Get computer choice (simulated input)
    computerChoice = input("Enter computer's choice (1-3): ")
    computerChoice = int(computerChoice)

    # Error handling for computer choice
    if computerChoice < 1 or computerChoice > 3:
        print("Error: Choice must be between 1 and 3.")
    else:
        # Array indexing (subtract 1 because lists are 0-indexed)
        playerName = choices[playerChoice - 1]
        computerName = choices[computerChoice - 1]

        # Print choices
        print("You chose:", playerName)
        print("Computer chose:", computerName)

        # Determine the winner
        if playerChoice == computerChoice:
            print("It's a tie!")
        elif playerChoice == 1 and computerChoice == 3:
            print("Rock beats Scissors - You win!")
        elif playerChoice == 2 and computerChoice == 1:
            print("Paper beats Rock - You win!")
        elif playerChoice == 3 and computerChoice == 2:
            print("Scissors beats Paper - You win!")
        else:
            print("You lose!")

        # String comparison
        if playerName != "Rock":
            print("You didn't pick the classic Rock...")
