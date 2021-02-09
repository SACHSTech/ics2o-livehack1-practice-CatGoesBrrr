'''
-------------------------------------------------------------------------------
Name:        minutes_days.py
Purpose:  Calculate days, hours, and minutes

Author:    Tan.C

Created:    date in 02/08/2021
------------------------------------------------------------------------------
'''
print("****** Minutes to Days and Hours ******")

# get number of minutes from user
number_of_minutes = int(input("Enter your minutes: "))

# compute days and hours
days = number_of_minutes // 1440
print("Days: " + str(days))
extra_minutes = number_of_minutes % 1440
hours = extra_minutes // 60
print("Hours: " + str(hours))

# output results
minutes = extra_minutes - hours * 60
print(str(number_of_minutes) + " minutes is " + str(days) + " day(s) " + str(hours)+" hour(s) and " + str(extra_minutes) + " minute(s)")