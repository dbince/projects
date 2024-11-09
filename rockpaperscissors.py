import random
choices = ["rock", "paper", "scissors"]
cpu_score = 0
player_score = 0
# player = input(choices)
rounds = input("How many rounds would you like to play?")

while cpu_score != int(rounds)+1 or player_score != int(rounds)+1:
    player = input("Rock, Paper or  Scissors?")
    computer = random.choice(choices)
    if cpu_score == rounds:
        print("The computer wins")
        break
    elif player_score == rounds:
        print("The player wins")
        break
    if player == computer:
        print('Tie')
    elif player == 'rock':
        if computer == 'paper':
            cpu_score += 1
            print("You lose", computer, "covers", player)
        elif computer == 'scissors':
            player_score += 1
            print("You win!", player, "crushes", computer)
    elif player == 'paper':
        if computer == 'scissors':
            cpu_score += 1
            print("You lose", computer, "cuts", player)
        elif computer == 'rock':
            player_score += 1
            print("You win!", player, "covers", computer)
    elif player == 'scissors':
        if computer == 'rock':
            cpu_score += 1
            print("You lose", computer, "crushes", player)
        elif computer == 'paper':
            player_score += 1
            print("You win!", player, "cuts", computer)
    elif player == 'end':
        print("Final Scores:")
        print("CPU:", cpu_score)
        print("Player:", player_score)
        break