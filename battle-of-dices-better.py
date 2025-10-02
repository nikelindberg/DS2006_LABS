
from dice import rollD6 

print("🎲 Welcome to Battle of Dices! 🎲")

# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0
round_number = 0

while player1_wins < 3 and player2_wins < 3:
    input("Press Enter to roll the dice...")
    
    round_number += 1 # New increment round counter 
    
# Roll dice using functions from dice.py
    player1_roll = rollD6()
    player2_roll = rollD6()

# Show the results
    input("\nPress ENTER to roll the dice...")
    print(f"\n--- Round {round_number} ---")
    print("Player 1 rolled: ", player1_roll)
    print("Player 2 rolled: ", player2_roll)
    input("\nPress ENTER to continue...")

# Determine round winner
    if player1_roll > player2_roll:
        player1_wins += 1
        round_winner = "Player_1"
        print("Player 1 wins this round!")
        print("Because ", player1_roll," is greater than ", player2_roll)
    elif player2_wins > player2_wins: 
        player2_wins += 1
        round_winner = "Player 2"
        print("Player 2 wins this round!")
        print("Because ", player2_roll," is greater than ", player1_roll)
    else: 
        round_winner = "Tie !"
        print("Amaaazzinng! This round has a tie!")
    
# Show result of the round"
        print("\n This round's winner:", round_winner)
        print("Score: Player 1:", player1_wins, "Player 2:", player2_wins)

# Game over 
print("\n GAME OVER")
print("Total rounds played:", round_number) # Show round count

if player1_wins == 3:
    print("Everyone is cheering for Player 1, the dominating CHAMPION of Battle of Dices! ")
elif player2_wins == 3:
    print("The crowd goes crazy!! Player 2 is the new Champion Battle of Dices! ")
else:
    print("This crazy Battle of Dices is not over yet! Who will win? ")
      
# We can print the game score:
print("\nThe game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

