import random
import matplotlib.pyplot as plt 

plot_roll_start = 2
plot_roll_end = 15
num_games = 1000000
x = []
y = []
for roll_number in range(plot_roll_start, plot_roll_end + 1):
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
    x.append(roll_number)
    y.append(1- (float(first_player_num_wins) / num_games))

plt.plot(x, y)
plt.xlabel('Start roll')
plt.ylabel('p2 win prob')
plt.show()
