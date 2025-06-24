# String
'''
    are immutable
'''

str1 = "Alice"
print(str1[0])

s1 = 'Single quoted'
s2 = "doubble quoted"
multiline = """My 
name
is 
Aditya"""
print(multiline)

print(len(multiline))

print("Aditya" in multiline)
print("name"not in multiline)

print(s1+s2)
print(s1)
print(s2)

txt = "The best things in the life are free!"
print(txt[2:10])

# all these does not effect the original string

print(f"upper: {txt.upper()}")# to make every letter uppercase
print(f"lower: {txt.lower()}")# to make every letter lowercase

print(f"title: {txt.title()}")# to make every first letter of every word uppercase

print(f"strip: {txt.strip()}")# remove white spaces from beginning and ending

print(f"split: {txt.split()}")# makes a list with each words of string. (seperated by the element provided in bracket)

print(f"replace: {txt.replace('The' ,'This')}")# replaces the with this

l=["Hello","Python"]
text=" "
print(f"join: {text.join(l)}")# Joins list into string with l[0]+ str + l[1] + str +l[3]....

print("find: ",txt.find("in"))# returns the index of the provided str (returns -1 if not found)

print(f"Count:", txt.count(" "))# returns the count of substring (returns 0 if not found)

print("satrtswith: ",txt.startswith("The"))# returns true if it starts with substring or false visa versa
print("endswith: ",txt.endswith("!"))# returns true if it ends with substring or false visa versa

name="Aditya"
sem=3
print("my name is :{}\nI am in sem :{}".format(name,sem)) # using format

print("HA"*3)# returns 3 times

print(txt)
# print(l)

