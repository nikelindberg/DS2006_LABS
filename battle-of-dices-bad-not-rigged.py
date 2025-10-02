import random

print("🎲 Welcome to Battle of Dices! 🎲")

# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0

# Round 1
player1__round1_roll = random.randint(1, 6)
player2__round1_roll = random.randint(1, 6)

# Round 2
player1__round2_roll = random.randint(1, 6)
player2__round2_roll = random.randint(1, 6)

# Round 3 
player1__round3_roll = random.randint(1, 6)
player2__round3_roll = random.randint(1, 6)

input("\nPress ENTER to roll the dice...")
print("Player 1 rolled: ", player1__round1_roll)
print("Player 2 rolled: ", player2__round1_roll)
input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1__round1_roll > player2__round1_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1__round1_roll," is greater than ", player2__round1_roll)
elif player2__round1_roll > player1__round1_roll:
    player2_wins += 1
    print("Player 2 wins this round!")
    print("Because ", player2__round1_roll," is greater than ", player1__round1_roll)
else: 
    print("Amaaazzinng! This round has a tie!")
    
        
# Now we need to check if either player won.
if player1_wins == 3:
    print("Everyone is cheering for Player 1, the dominating CHAMPION of Battle of Dices! ")
elif player2_wins == 3:
    print("The crowd goes crazy!! Player 2 is the new Champion Battle of Dices! ")
else:
    print("This crazy Battle of Dices is not over yet! Who will win? ")
    
  
# We can print the game score:
print("\nThe game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")


# Since none of them would have won after 1 round, we could copy this code several times
# until we have enough times to make sure someone wins.


# Round 2

input("\nPress ENTER to roll the dice...")

print("Player 1 rolled: ", player1__round2_roll)

print("Player 2 rolled: ", player2__round2_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1__round2_roll > player2__round2_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1__round2_roll," is greater than ", player2__round2_roll)
elif player2__round2_roll > player1__round2_roll: 
    player2_wins += 1
    print("Player 2 wins this round!")
    print("Because ", player2__round2_roll," is greater than ", player1__round2_roll)
else: 
    print("Amaaazzinng! This round has a tie!")
    
        
# Now we need to check if either player won.
if player1_wins == 3:
    print("Everyone is cheering for Player 1, the dominating CHAMPION of Battle of Dices! ")
elif player2_wins == 3:
    print("The crowd goes crazy!! Player 2 is the new Champion Battle of Dices! ")
else:
    print("This crazy Battle of Dices is not over yet! Who will win? ")
    
  
# We can print the game score:
print("\nThe game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")


# Round 3

# Variables to keep track of the score:
input("\nPress ENTER to roll the dice...")

print("Player 1 rolled: ", player1__round3_roll)

print("Player 2 rolled: ", player2__round3_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1__round3_roll > player2__round3_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1__round3_roll," is greater than ", player2__round3_roll)
elif player2__round3_roll > player1__round3_roll: 
    player2_wins += 1
    print("Player 2 wins this round!")
    print("Because ", player2__round3_roll," is greater than ", player1__round3_roll)
else: 
    print("Amaaazzinng! This round has a tie!")
    
        
# Now we need to check if either player won.
if player1_wins == 3:
    print("Everyone is cheering for Player 1, the dominating CHAMPION of Battle of Dices! ")
elif player2_wins == 3:
    print("The crowd goes crazy!! Player 2 is the new Champion Battle of Dices! ")
else:
    print("This crazy Battle of Dices is not over yet! Who will win? ")
    
  
# Showing the result of each round for Player 1 and Player 2:
print("\nThe rolls for Player 1 were:", player1__round1_roll, player1__round2_roll, player1__round3_roll)
print("\nThe rolls for Player 2 were:", player2__round1_roll, player2__round2_roll, player2__round3_roll)
