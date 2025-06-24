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

''' Collection of orderred , immutable , declared using () , similer to tupple but the element can't be modified ,  allow duplicates'''

num = (1,2,3,4)

colors= "red" , "green" , "blue" #n tupples without paranthesis (Tupple packing)

# num[3]=3
print(len(num))
print(len(colors))
