while True:
    print("1.Addition 2.Substraction 3.Multiplication")
    choice = int(input("Enter your choice: "))
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == 1:
        print("The result is ",a+b)
    elif choice ==2:
        print("The result is ",a-b)
    elif choice ==3:
        print("The result is ",a*b)
    else:
        print("Invalid input")

