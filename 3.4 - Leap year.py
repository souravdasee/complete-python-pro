#Code_challenge

# Instructions
# Write a program that works out whether if a given year is a leap year.
# A normal year has 365 days, leap years have 366, with an extra day in February.
# The reason why we have leap years is really fascinating, this video does it more justice:

# https://www.youtube.com/watch?v=xX96xng7sAE

# This is how you work out whether if a particular year is a leap year.

# on every year that is evenly divisible by 4 
# **except** every year that is evenly divisible by 100 
# **unless** the year is also evenly divisible by 400

# >>>>>>>>>>>>>>>>>>>>>>Hint<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# If you really get stuck, you can see the flow chart I created: https://bit.ly/36BjS2D
#---------------------------------------------------------------------------------------------



# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0 :
    if year % 100 == 0 :
        if year % 400 == 0 :
            print ("Leap year.")
        else :
            print ("Not leap year.")
    else :
        print ("Leap year.")
else :
    print ("Not leap year.")