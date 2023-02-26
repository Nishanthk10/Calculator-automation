def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b


while True:
    print("1.Addition 2.Substraction 3.Multiplication")
    choice = int(input("Enter your choice: "))
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == 1:
        print("The result is ",add(a,b))
    elif choice ==2:
        print("The result is ",sub(a,b))
    elif choice ==3:
        print("The result is ",mult(a,b))
    else:
        print("Invalid input")

