from dice import rollD6

print("🎲 Welcome to Battle of Dices! 🎲")
# Number of wins needed to win the game:
winning_score = 3
# Array for storing the names of the players:
player_names = []
# Array for storing the number of wins for each player:
player_wins = []
#Obtain the number of players:
number_of_players = int(input("How many players?: "))
#For loop to obtain the player names:
for i in range(number_of_players):
    name = input(f"What is the name of Player {i+1}?: ")
    player_names.append(name)    
# Initialize scores and rolls
for i in range(number_of_players):
    player_wins.append(0)    
# Initialize player rolls as empty lists for each player
player_roll_history = [] # This will be a nested list
for i in range(number_of_players):
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
        roll = rollD6()
        current_rolls.append(roll)
        player_roll_history[i].append(roll)
        print(f"Player {player_names[i]} rolled: {roll}")        
#... still in the while gameover is False:
#Obtain the highest roll this round:
    max_roll = max(current_rolls)
#Winners will store information about who won this round:
    winners = []
#Search for all players who got the highest roll:
    for j in range(len(current_rolls)):
        if current_rolls[j] == max_roll:
            winners.append(player_names[j])
            player_wins[j] += 1
            if player_wins[j] == winning_score:
                print(f"{player_names[j]} wins the game! ")
                gameover = True
        
    print(f"Winners of this round are: {winners}")        
# Game over 
print("\nGAME OVER")
print("Total rounds played:", rounds) # Show round count
# Save results to a file
filename = input("Enter the filename to save the results: ")
with open(filename, "w") as file:
    for round_number in range(rounds):
        file.write(f"Round {round_number+1}: ")
        rolls_str = "" # Start with an empty string
        for i in range(number_of_players):
            rolls_str += (f"{player_names[i]} rolled {player_roll_history[i][round_number]}")
        if i < number_of_players - 1: # Adds a comma after each, except the last one
            rolls_str += ", "
    file.write(rolls_str + "\n")
    
    print(f"Results saved to {filename}")