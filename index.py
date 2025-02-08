from random import choice
import time

moves = {'Rock': '🪨', 'Paper': '📄', 'Scissors': '✂'}
player = input('Rock, Paper or Scissors?').lower()
computer = choice(list(moves.keys()))

print(f"\nYou: {moves[player]}")
time.sleep(0.5)
print(f"Computer: {moves}[computer]")

#Game Logic

if player == computer:
    print('❤️Tie!')

elif (player == 'Rock' and computer == 'Scissors')  or\
     (player == 'Paper' and computer == 'Rock')  or\
     (player == 'Scissors' and computer == 'Paper'):
    print("You win!")
else:
    print("You Lose")