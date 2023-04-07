"""
This program simulates a dice gambling game where a six sided die is rolled, if values
of 1,2, or 3 are rolled then the game is over. If values of 4, 5, or 6 are rolled then
the player receives the corresponding amount of money ($4, $5, $6) and the game continutes.
The program simulates this game 10,000 times.
"""
#import the random module
import random

#create variables needed for statistcs
total_winnings = 0 
non_zero_games = 0
max_winnings = 0

#running the dice gambling game simulation 10,000 times using the randint function to simulate rolling a dice
for i in range (10000):
    winnings = 0 
    while True:
        roll = random.randint(1,6)
        if roll == 1:
            break
        elif roll == 2:
            break
        elif roll == 3:
            break
        elif roll == 4:
            winnings += 4
        elif roll == 5:
            winnings += 5
        else:
            winnings += 6 
    if winnings > 0:
        non_zero_games += 1
        total_winnings += winnings 
    if winnings > max_winnings:
        max_winnings = winnings

#calculating non-zero probability and average winnings statistics
non_zero_game_probability = (non_zero_games / 10000) * 100
average_winnings = total_winnings / 10000 

#printing results of the simulation and the statistics calculated
print("Probability of winning a non-zero amount = ", round(non_zero_game_probability,2) ,"%")
print("The average amount won = $", round(average_winnings,2))
print("Max amount won = $", max_winnings)

'''
1) How likely do you think it is to win at least $4?: The simulation tells us it is
50% likely to win at least 4 dollars. The reason for this is because you have a 50% chance of 
winning a non-zero amount and since all non-zero amounts are at least over $4 than it is
a 50% chance.

2) Would you pay $3 for a chance to play this game? Why or why not? How about $4?:
We would be willing to pay $3 for a chance to play this game this is because, according to
our simulation, you have a 50% change of a non-zero amount. In the case of paying $3 to
play the game, you would be profitting 50% of the time. We would not pay $4 to play this
game because there would be only be a 33% chance of profitting as only rolls of 5 or 6 
would make us money.

'''