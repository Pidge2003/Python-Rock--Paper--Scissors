from random import choice
import time

moves = {'rock': '🪨', 'paper': '📄', 'scissors': '✂'}
player = input('rock, paper or scissors?').lower()
computer = choice(list(moves.keys()))

print(f"\nYou: {moves[player]}")
time.sleep(0.5)
print(f"Computer: {moves}[computer]")

#Game Logic

if player == computer:
    print('❤️Tie!')

elif (player == 'rock' and computer == 'scissors')  or\
     (player == 'paper' and computer == 'rock')  or\
     (player == 'scissors' and computer == 'paper'):
    print("You win!")
else:
    print("You Lose")