import random

choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

while True:
    player = input("rock, paper, scissors (or quit): ").lower()
    if player == "quit":
        break
    if player not in choices:
        print("Not a valid choice.")
        continue

    computer = random.choice(choices)
    print("Computer picked:", computer)

    if player == computer:
        print("Tie.")
    elif player == "rock" and computer == "scissors" or player == "paper" and computer == "rock" or player == "scissors" and computer == "paper":
        print("You win this round.")
        player_score += 1
    else:
        print("Computer wins this round.")
        computer_score += 1

    print("Score:", player_score, "-", computer_score)

