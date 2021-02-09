'''
-------------------------------------------------------------------------------
Name:       days_hours.py
Purpose:  Converts hours to days and hours

Author:    Tan.C

Created:    date in 02/08/2021
------------------------------------------------------------------------------
'''
print("****** Hours to Days and Hours ******")

# get number of hours from user
number_of_hours = float(input("Enter your hours: "))

# compute days and hours
days = round(number_of_hours // 24)
hours = number_of_hours % 24

# output results
print(str(number_of_hours) + " hour(s) = " + str(days) + " day(s) and " + str(hours)+" hour(s).")