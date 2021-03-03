"""
-------------------------------------------------------------------------------
Name:     problem2.py
Purpose:  This program allows Tony to enter the distance driven for each day until the total distance driven surpasses 100km. 

Author:   Tam.S

Created:  03/03/2021
------------------------------------------------------------------------------
"""
# print headers
print("***** Welcome to the DoorDash Distance Tracker ******")
print("")

print("** Travel Log **")

# set variables
distance = 0
days = 0

# loop until distance is greater than 100km and count the days
while distance <= 100:
  traveled = int(input("Enter the distance travelled for the day: "))
  distance += traveled
  days += 1

# calculate average
average = round(distance/days)

# output results
print("")
print("** Summary **")
print ("It took", days, "days to surpass 100km driven.")
print("The average distance driven per day is", average, "km.")