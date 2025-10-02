from dice import rollD6

print("🎲 Welcome to Battle of Dices! 🎲")

list_of_player1_rolls = [] # New: Lists to store all rolls
list_of_player2_rolls = []

# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0
round_number = 0

# Game loop: first to 3 wins
while player1_wins < 3 and player2_wins < 3:    
    round_number += 1 # Increment round counter 
    
    # Roll dice using functions from dice.py
    player1_roll = rollD6()
    player2_roll = rollD6()

    # Show the results
    input("\nPress ENTER to roll the dice...")
    print(f"\n--- Round {round_number} ---")
    print("Player 1 rolled: ", player1_roll)
    list_of_player1_rolls.append(player1_roll) 
    print("Player 2 rolled: ", player2_roll)
    list_of_player2_rolls.append(player2_roll)
    input("\nPress ENTER to continue...")

    # Determine round winner
    if player1_roll > player2_roll:
        player1_wins += 1
        round_winner = "Player_1"
        print("Player 1 wins this round!")
        print("Because ", player1_roll," is greater than ", player2_roll)
    elif player2_roll > player1_roll: 
        player2_wins += 1
        round_winner = "Player 2"
        print("Player 2 wins this round!")
        print("Because ", player2_roll," is greater than ", player1_roll)
    else: 
        round_winner = "Tie !"
        print("Amaaazzinng! This round has a tie!")
    
    # Show result of the round
        print("\n This round's winner:", round_winner)
        print("Score: Player 1:", player1_wins, "Player 2:", player2_wins)

# Game over 
print("\n GAME OVER")
print("Total rounds played:", round_number) # Show round count

# Final winner
if player1_wins == 3:
    print("Everyone is cheering for Player 1, the dominating CHAMPION of Battle of Dices! ")
elif player2_wins == 3:
    print("The crowd goes crazy!! Player 2 is the new Champion Battle of Dices! ")
else:
    print("This crazy Battle of Dices is not over yet! Who will win? ")
      
# We can print the game score:
print("\nThe game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# GAME SUMMARY
print("\nGame Summary:")
table_rows = ""
table_header = ("| Round | Player 1 | Player 2 |\n"
"-------------------------------------------\n")



for i in range(round_number):
     row = f"{i+1:<5} | {list_of_player1_rolls[i]:<8} | {list_of_player2_rolls[i]}\n"
     table_rows += row
     
     
# New: Saving the Game Summary to a file
filename = input("Enter the filename to save results: ")

with open(filename, "w") as file:   # "w" = write mode
        file.write(table_header)
        file.write(table_rows)
        
print("Results saved to", filename)
     