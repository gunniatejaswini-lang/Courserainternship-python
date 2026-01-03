import random

# Function to display game rules
def show_rules():
    print("\n===== ROCK PAPER SCISSORS GAME =====")
    print("Rules:")
    print("1. Rock beats Scissors")
    print("2. Scissors beats Paper")
    print("3. Paper beats Rock")
    print("Type 'rock', 'paper', or 'scissors' to play")
    print("Type 'exit' to quit the game")
    print("===================================\n")

# Function to get computer choice
def computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# Function to decide winner
def decide_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

# Main game function
def play_game():
    user_score = 0
    computer_score = 0
    round_number = 1

    show_rules()

    while True:
        print(f"\n--- Round {round_number} ---")
        user = input("Enter your choice (rock/paper/scissors): ").lower()

        if user == "exit":
            print("\nGame Over!")
            break

        if user not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        computer = computer_choice()

        print(f"You chose: {user}")
        print(f"Computer chose: {computer}")

        result = decide_winner(user, computer)

        if result == "tie":
            print("Result: It's a TIE 🤝")
        elif result == "user":
            print("Result: You WIN 🎉")
            user_score += 1
        else:
            print("Result: Computer WINS 💻")
            computer_score += 1

        print("\nSCOREBOARD")
        print(f"Your Score     : {user_score}")
        print(f"Computer Score : {computer_score}")

        round_number += 1

        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThanks for playing!")
            break

# Start the game
play_game()
