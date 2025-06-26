#### Compile time polymorphism ####

'''
Operating overloading allows custom classes to define how operator like (+, - , etc) behavewhen used class object. It makes custom objectsbehave like built in types 
''' 
# class Point:
#     def __init__(self, x ,y):
#         self.x=x
#         self.y=y

#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)

# P1=Point(2,4)
# P2=Point(1,4)
# P3=P1+P2
# print(P3.x, P3.y)


# class Book:
#     def __init__(self, title, pages):
#         self.title=title
#         self.pages=pages

#     def __add__(self, other):
#         return self.pages + other.pages

# b1=Book("Python Introduction", 300)
# b2=Book("Harry Potter", 450)
# print(b1+b2)



# class Student:
#     def __init__(self, name, roll):
#         self.name = name
#         self.roll = roll

#     def __eq__(self, value):
#         return self.roll == value.roll

# s1 = Student("Aayush", 44)
# s2 = Student("Aadi", 48)
# s3 = Student("Jay", 44)

# print(s1 == s3)
# print(s1 == s2)


##### File hanling



"""
There are 4 different modes to open a file
1. Read--> "r" is a default value and used to only read a file(will give error if the file does not exists)
2. Append--> "a" opens a file for appending (adding data to end of a file) creates file if it does not exists.
3. Write --> "w" opens a file for writing (will overwrite the data in the file) and will create file if it does not exists.
4. Create --> "x" will create a specific file and return error if the file exists.

 In addition you can specify should the file be handled as binary or text mode.
 "t" is for default
 "b" is for binary mode

"""

'''
funtions of file handeling:
read()--> reads whole file
readline()--> reads file line by line
readlines()--> it reads all lines into a list
(if you have already called .read() or .readlines() method earlier the file pointer is at end of the file and returns empty string)
'''


f= open("demo.txt","r")
# print(f.read())

line1= f.readline()
line2= f.readline()
# print(line1,line2)

lines= f.readlines()
for i in lines:
    # print(i.strip())
    pass


### write
'''
Write Method functions
write()--> will write a line
writelines()--> will write a list of strings
'''
f1=open("new.txt","w")
# f1.write("Hello World")
# f1.write("\njust a World")
l1=["apple\t","banana"]
f1.writelines(l1)

### append 
'''
append will add data at the end of file
'''
f2 =open("new.txt","a")
f2.write("Hello")

f.close()
f1.close()
f2.close()
# binary
"""
binary mode is used for image, audio or any non text data
"""

# with open("image.jfif","rb") as f:
#     data = f.read()

