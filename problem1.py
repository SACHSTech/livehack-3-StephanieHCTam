"""
-------------------------------------------------------------------------------
Name:     problem1.py
Purpose:  This program determines which group a player is placed in.

Author:   Tam.S

Created:  03/03/2021
------------------------------------------------------------------------------
"""

print("****** Tournament Tracker ******")

# ask user for their team results
print("Enter the wins and losses for your team: ")

# set total variable
total = 0

# for loop
for i in range(6):
  result = input("Game " + str(i + 1) + " (W/L): ")
  if result == 'W':
    total += 1

# output team placement
if total == 5 or total == 6:
  print("Your team is in Group 1.")
if total == 3 or total == 4:
  print("Your team is in Group 2.")
if total == 1 or total == 2:
  print("Your team is in Group 3.")
if total == 0:
  print("Your team is eliminated from the tournament.")