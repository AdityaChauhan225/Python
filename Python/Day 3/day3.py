
import mymod as md

# md.num()

# exception handling

''' exception is a event that disrupts the normal flow of the program..
for example 
Types of error:
ZeroDivisionError :- when try to divide by zero
ValueError:-
TypeError:-
IndexError:-
KeyError:-Will occur in dict when error in keys
FileNotFound:-
AttributeError:-

'''
# a=2/0 will return error

# try:
#     n1= int(input("n1:"))
#     n2= int(input("n2:"))
#     print(n1/n2)
# except ZeroDivisionError:
#     print("not divisible by zero")
# except ValueError :
#     print("Enter valid number")
# except TypeError:
#     pass
# else:
#     print("Else")
# finally:
#     print("hey")

try:
    inp=input("Are you stuck : Yes / NO ?\n")
    if inp.lower()=="no":
        print("Someone is on the way to your rescue.")
    elif inp.lower()=="yes":
        print("OK!")
except Exception as e:
    print("Are you sure you entred right ?")
    print(e)
