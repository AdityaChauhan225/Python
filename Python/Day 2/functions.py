# Function
''' Reusable block of code that performs a specific task '''

# to define a function use def

# Arugments in function

'''
positional 
keyword
'''

def greet(user="Aditya"):#default
    print(f"Hello {user}, Welcome")

greet("Aadi")# positional arg
greet(user="aadi")# keyword arg
greet()# uses default

# variable length argument (*args, **kwargs)

def greetuser(*arg):
    for n in arg:
        print(f"Hello,{n}")

greetuser("Alice", "Bob","Charlie")

def dis_info(**kwarg):
    for k, v in kwarg.items():
        print(f"{k}:{v}")

dis_info(name="aadi",age=20,city="paris")

def demoFun(*arg,**kwarg):
    print(f"args:{arg}\nkwargs:{kwarg}")

demoFun("a","b","c",name="Alice",age=20,city="paris")