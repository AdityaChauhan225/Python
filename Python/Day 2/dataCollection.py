# non primitive data types

# # list
# '''
# Ordered , allow duplicates , mutable 
# '''
# list = [1,2,"Kiwi",4,"Aadi",'Aayush',2.34,False,2,3,4] #can include multiple datatypes 

# # print(list)

# list[2]="Orange"

# # print(list)

# list[-3]="Mango"

# # print(list)


# # operations

# ''' Append , Pop , Insert , Extend , Remove , len , Index , count , Sort , Reverse , Copy , Clear , '''

# list.append(22)

# list.pop()

# print(list[1:3])

# list.insert(3,False) # index , value to be inserted
# print(list)

# l1 =[2,5,543,2]
# list.extend(l1)
# print(list)
# print(l1)

# l1.remove(2)

# print(len(l1))
# print(list.index(4))
# print(list)
# print(list.count(2))
# l2=[51,89,23,90,101]
# l2.sort()
# print(l2)
# l2.reverse()
# print(l2)
# print(l2.copy())
# l2.clear()
# print(l2)





###### Tupple ######

''' Collection of orderred , immutable , declared using () , similer to tupple but the element can't be modified ,  allow duplicates, are faster than list , provides data integrity(Data not changed by accident )  '''

# num = (1,2,3,4)

# colors= "red" , "green" , "blue" #n tupples without paranthesis (Tupple packing)

# # num[3]=3
# print(len(num))
# print(len(colors))

tup1= (1,2,3,3,3,3)
# tup2 = (4,5,6)
# print(tup1+tup2) 
# print(tup1*3)

# print(tup1.count(3))
# print(tup1.index(2))


# # tupple unpacking 
 
# person = ("joy", 27 , "Developer")
# name,age,professtion = person

# print(name)

#  these will not work in tupples
# tup1.append(1)
# tup1.sort()
# tup1.pop()
# tup1.remove(2)

# Set
''' unordered , unique , mutable , declared using {}'''
set1={1,4,4,5,3,74,7,7,5}

''' add() , remove() , discard() , len() , pop()removes first element , clear()empties set , Difference() , symmetric_difference()
'''
# frozen set
''' cannot modify this set'''

# set1.add(11)
# set1.remove(1)
# # set1.remove(12) # will retur key error as 12 is not in set

# set1.discard(4)
# set1.discard(12)# it will not give error even if the element is not present

# print(len(set1))

# print(4 in set1)
# print(5 in set1)
# print(set1)

# set1.pop()
# set1.clear()
# print(set1)

s1 = {1,2,3,4}
s2 = {3,4,5,6}

print(s1|s2)
print(s1 or s2)
print(s1.union(s2))

print(s1&s2)
print(s1 and s2)
print(s1.intersection(s2))

print(s1.issubset(s2))

print(s1-s2)
print(s1.difference(s2))

print(s1^s2) # either in set1 or set2 not in both sets
print(s1.symmetric_difference(s2))

sq = {x**2 for x in range(1,6)} 
print(sq)

# frozen set
''' cannot modify this set'''
se1 = frozenset([1,23,4]) 

##### Dictionary

''' mutable , unordered , key-value pairs (key must be unique and immutable) 
'''

student={
    "roll" :1,
    "name":"Aditya",
    "Branch":"CSE"
}
print(student["Branch"])

person= dict(name="Aadi", age= 20, city="Jaipur")
print(person["city"])

student["college"]='PIET'
print(student)

person["city"]='Gurugram'
print(person)

student.pop("college")
print(student)

del student["Branch"]
print(student)

student.clear()
print(student)


# Nested dictionary
students = {
    101:{"name":"Aditya","College":"Piet","Age":20},
    102:{"name":"Aayush","College":"Pit","Age":21},
    103:{"name":"Sidhart","College":"Piet","Age":19}
}

students[102]["Age"] = 20
print(students[102]["Age"] )
