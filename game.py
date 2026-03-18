import random

# Options for the game
choices = ["rock", "paper", "scissors"]

# Function to decide the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif(user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "scissors" and computer_choice == "paper") or \
        (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

# Main game loop
while True:
    user_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
    if user_choice == "quit":
        print("Thanks for playing!")
        break
    elif user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)
