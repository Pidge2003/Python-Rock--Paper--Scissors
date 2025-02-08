from random import choice
import time

moves = {'rock': '🪨', 'paper': '📄', 'scissors': '✂'}

while True:
    player = input('Choose either rock, paper or scissors?').lower()
    if player not in moves:
        print("Invalid input. Please choose rock, paper, or scissors.")
        continue

    computer = choice(list(moves.keys()))

    print(f"\nYou: {moves[player]}")
    time.sleep(0.5)
    print(f"Computer: {moves[computer]}")

    if player == computer:
        print('❤️Tie!')
    elif (player == 'rock' and computer == 'scissors') or\
         (player == 'paper' and computer == 'rock') or\
         (player == 'scissors' and computer == 'paper'):
        print("You win!")
    else:
        print("You Lose")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break