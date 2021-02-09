'''
-------------------------------------------------------------------------------
Name:        windchill.py
Purpose:  Find windchill

Author:    Tan.C

Created:    date in 02/08/2021
------------------------------------------------------------------------------
'''
print("****** Windchill Calculator ******")

# get temperature and windspeed from user
temperature = float(input("Enter your temperature: "))
windspeed = float(input("Enter the windspeed: "))

# compute windchill
windchill = 13.12 + (0.6215 * temperature) - (11.37 * windspeed**0.16) + (0.3965 * temperature * windspeed**0.16)

# output windchill
print("Windchill is: " + str(windchill))