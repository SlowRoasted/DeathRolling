import random

roll_number = 2
num_games = 1000000
first_player_num_wins = 0

for i in range(num_games):
    last_rolled_number = roll_number
    while True:
        last_rolled_number = random.randrange(last_rolled_number) + 1
        if last_rolled_number == 1:
            break
        last_rolled_number = random.randrange(last_rolled_number) + 1
        if last_rolled_number == 1:
            first_player_num_wins += 1
            break
        
print(f'Out of {num_games}, player rolling first won {first_player_num_wins}, {float(first_player_num_wins)/num_games * 100}%')