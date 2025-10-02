from dice import rollD6, rollD20 

print("🎲 Welcome to Battle of Dices! 🎲")

# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0
round_number = 0

while player1_wins < 3 and player2_wins < 3:
    input("Press Enter to roll the dice...")
    
    round_number += 1 # New increment round counter 
    
# Roll dice using functions from dice.py
    player1_rollD6 = rollD6()
    player2_rollD6 = rollD6()
    
    player1_rollD20 = rollD20()
    player2_rollD20 = rollD20()
    
    player1_total = player1_rollD6 + player1_rollD20
    player2_total = player2_rollD6 + player2_rollD20 

# Show the results
    print(f"\n--- Round {round_number} ---")
    print("Player 1 rolled: D6 =", player1_rollD6, ", D20 =", player1_rollD20, " | Total =", player1_total)
    print("Player 2 rolled: D6 =", player2_rollD6, ", D20 =", player2_rollD20, " | Total =", player2_total)
    input("\nPress ENTER to continue...")

# Determine round winner
    if player1_total > player2_total:
        player1_wins += 1
        round_winner = "Player 1"
        print("Player 1 wins this round!")
        print("Because ", player1_total," is greater than ", player2_total)
    elif player2_total > player1_total: 
        player2_wins += 1
        round_winner = "Player 2"
        print("Player 2 wins this round!")
        print("Because ", player2_total," is greater than ", player1_total)
    else: 
        round_winner = "Tie !"
        print("Amaaazzinng! This round has a tie!")
        
# Show round result
print("\nThis round's winner with the biggest sum:", round_winner)
print("Score: The game score is Player1 ", player1_wins, "VS. ", player2_wins, " Player 2.")