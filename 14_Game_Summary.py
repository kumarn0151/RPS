from numpy import percentile


game_summary = []

rounds_lost = 0 
rounds_drawn = 0 
rounds_played = 5 

for item in range(0, 5):
    result = input("choose result: ")

    outcome = "Round {}: {}".format(item, result)

    if result == "lose":
        rounds_lost += 1 
    elif result == "tie":
         rounds_drawn += 1 

    game_summary.append(outcome)

rounds_Won = rounds_played - rounds_lost - rounds_drawn

# **** Calculate Game Stats ***** 
percent_win = rounds_Won/ rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100
percent_draw = rounds_drawn / rounds_played * 100

print()
print("****** Game History ******")
for game in game_summary:
    print(game)

print()

# display game stats with % values to the nearest whole number
print("****(** Game Statstics *****")
print("Win: {}, ({:.0f}\nloss: {}, ({:.0f}%)\nTie: {}, ({:.0f}%)".format(rounds_Won,percent_win, rounds_lost, percent_lose, rounds_drawn, percent_draw))