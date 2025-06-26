## os 

'''
We can handle files using os module

it helps to access files, directries, enviornment variables and run system programs

when you need to automate file tasks for eg: rename or organise files , building tools that need directory access , running scripts that uses system level information 

'''

import os

print(os.getcwd()) # --> returns path of current directory

print(os.path.exists("new.txt")) # --> returns true if the file exists
print(os.path.exists("new1.txt")) # --> returns false if the file does not exist

# os.rename("new.txt","new1.txt") # --> changes the name of the file
# os.remove("new.txt") # --> will remove the file

# organize all the question in numeric order with the correct answers and ignore the duplicates and incomplete questions