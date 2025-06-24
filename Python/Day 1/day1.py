'''
    python
        made by guido van rossum
        interpreted (executed line by line)
        it is interpreted and compiled
        it is high level language
        it is easy to read and write.
        it has a vast collection of libraries
        it is dynamically typed(you don't need to declare variable types,  automatically determined at runtime)
        it is cross platform (It can run on various os without any change)              
        it is very varatile (used in data analysis, web development, game development, ML/AI)                      
        it's name is derived from a tv show 
        it is platform independent

    variable
        it must start with a letter
        should not start with special character
        can be reassigned a variable to a different datatype 

    data types
        str
        int
        float    
        bool
        NoneType (just like null (no value)) (to declare = None)
'''

print("Hello world\n")
name ="BOB"
age = 20
none = None
print(f"name:{name}, age:{age}\n")
print(type(name))
print(type(age))
print(type(none))




# multiple variable declaration 

x,y,z =10,20,30

print(x)
print(y)
print(z)



# Input

# subject = input("Enter a subject you know:-\n")
# print(type(subject))

num1 = int(input("Enter Base:"))
num2 = int(input("Enter Power:"))
print(f"{num1} ** {num2} = {num1**num2}")




