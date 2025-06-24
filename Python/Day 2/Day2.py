# Loops 
# for loop

# for i in range(2,30,3):
#     print(i)

password = "Abc@123"

# for i in range(3,0,-1):
#     user = input("Enter password:-")
#     if user == password:
#         print("Welcome")
#         break
#     else:
#         print("Access Denied")
#         print(f"attemp left {i-1}")


max = 3
while max>0:
    user = input("Enter password:-")
    if user == password:
        print("Welcome")
        break
    else:
        print("Access Denied")
        print(f"attemp left {max-1}")
    max-=1