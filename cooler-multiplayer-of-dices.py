from dice import rollD6, rollD8

print("🎲 Welcome to Battle of Dices! 🎲")

winning_score = 3
player_names = []
player_wins = []
number_of_players = int(input("How many players?: "))
player_roll_history = [] # This will be a nested list
#For loop to obtain the player names:
for i in range(number_of_players):
    name = input(f"What is the name of Player {i+1}?: ")
    player_names.append(name)    
# Initialize scores and rolls
for i in range(number_of_players):
    player_wins.append(0)    
    player_roll_history = [[] for _ in range(number_of_players)]
    player_roll_history.append([])

gameover = False
rounds = 0   
 
# Game loop: first to 3 wins
while gameover is False:
    print(f"Round {rounds+1}:")
    rounds += 1
    # Dice roll for each player in the current round:
    current_rolls = []
    # We need to roll the dice for each player:
    for i in range(number_of_players):
        d6 = rollD6()
        d8 = rollD8()
        total = d6 + d8
        
        current_rolls.append(total)
        player_roll_history[i].append((d6, d8, total)) # store all rolls
        
        print(f"Player {player_names[i]} rolled a D6={d6}, D8={d8} (Total={total}): ")  
         
#... still in the while gameover is False:
#Obtain the highest roll this round:
    max_roll = max(current_rolls)
    # Winners will store information about who won this round:
    winners = []
#Search for all players who got the highest roll:
    for j in range(len(current_rolls)):
        if current_rolls[j] == max_roll:
            winners.append(player_names[j])
            player_wins[j] += 1
            if player_wins[j] == winning_score:
                print(f"{player_names[j]} wins the game! 🎉")
                gameover = True
        
    print(f"Winners of this round are: {winners}")        
# Game over 
print("\nGAME OVER")
print("Total rounds played:", rounds) # Show round count
# Save results to a file
filename = input("Enter the filename to save the results: ")
with open(filename, "w") as file:
    for round_number in range(rounds):
        rolls = []
        for i in range(number_of_players):
            d6, d8, total = player_roll_history[i][round_number]
            rolls.append(f"{player_names[i]} rolled D6={d6}, D8={d8}, Total={total}")
        line = f"Round {round_number+1}: " + ", ".join(rolls) + "\n"
        file.write(line) 
    print(f"Results saved to {filename}")