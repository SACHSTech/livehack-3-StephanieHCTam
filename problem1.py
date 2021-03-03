"""
-------------------------------------------------------------------------------
Name:     problem1.py
Purpose:  This program determines which group a player is placed in.

Author:   Tam.S

Created:  03/03/2021
------------------------------------------------------------------------------
"""

print("****** Welcome to the Tournament Tracker ******")
print("")

# ask user for their team results
print("Enter the wins and losses for your team: ")

# set win variable
wins = 0

# ask for user input from 6 games and count the number of wins 
for i in range(6):
  result = input("Game " + str(i + 1) + " (W/L): ")
  if result == 'W':
    wins += 1

# check conditions and output results
if wins == 5 or wins == 6:
  print("Your team is in Group 1.")
elif wins == 3 or wins == 4:
  print("Your team is in Group 2.")
elif wins == 1 or wins == 2:
  print("Your team is in Group 3.")
else:
  print("Your team is eliminated from the tournament.")