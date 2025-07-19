import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "user"
    else:
        return "computer"

def print_instructions():
    print("\nWelcome to Rock, Paper, Scissors!")
    print("Instructions:")
    print(" - Type 'rock', 'paper', or 'scissors' to make your move.")
    print(" - Rock beats scissors, scissors beat paper, paper beats rock.")
    print(" - Type 'quit' to end the game at any time.\n")

def main():
    user_score = 0
    computer_score = 0
    round_number = 1

    print_instructions()

    while True:
        print(f"\n--- Round {round_number} ---")
        user_choice = input("Your choice (rock/paper/scissors): ").lower()

        if user_choice == 'quit':
            break
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid input. Please choose 'rock', 'paper', or 'scissors'.")
            continue

        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score -> You: {user_score} | Computer: {computer_score}")

        play_again = input("Play another round? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            break
        round_number += 1

    print("\nThanks for playing!")
    print(f"Final Score -> You: {user_score} | Computer: {computer_score}")

if __name__ == "__main__":
    main()
