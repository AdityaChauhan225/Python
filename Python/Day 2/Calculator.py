
def sum(a,b):
    print(f"{a} + {b} = {a+b}")

def sub(a,b):
    print(f"{a} - {b} = {a-b}")

def div(a,b):
    if b==0:
        print("Cannot divide by 0")
    else:
        print(f"{a} / {b} = {a/b}")

def mul(a,b):
    print(f"{a} * {b} = {a*b}")

def pow(a,b):
    print(f"{a} ** {b} = {a**b}")


num1 = int(input("Num1-> ")) 
op= input("enter Operator->")
num2 = int(input("Num2-> "))

match op:
    case "+":
        sum(num1,num2)
    case "-":
        sub(num1,num2)
    case "/":
        div(num1,num2)
    case "*":
        mul(num1,num2)
    case "**":
        pow(num1,num2)
