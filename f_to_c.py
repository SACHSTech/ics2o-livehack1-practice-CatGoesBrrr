'''
-------------------------------------------------------------------------------
Name:        f_to_c.py
Purpose:  Convert Fahrenheit to Celcius

Author:    Tan.C

Created:    date in 02/08/2021
------------------------------------------------------------------------------
'''
print("****** Fahrenheit to Celsius Converter ******")

# get Fahrenheit from user
fahrenheit = float(input("Enter your degrees: "))

# Celcius formula
celcius = (degrees - 32) * 5 / 9

# Output celcius
print("The temperature in celcius is " + str(celcius) + "°.")