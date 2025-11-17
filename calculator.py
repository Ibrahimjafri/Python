import math

print("Select Mode:")
print("                       ")
print("1) Addition")
print("2) Subtraction")
print("3) Multiplication")
print("4) Division")
print("5) Square Root")
print("6) Cube Root")
print("                       ")

choice = input("Enter your mode (1-6): ")
print("                                              ")

if choice == '5':
    number = float(input("Enter a number: "))
    if number < 0:
        print("Cannot take the square root of a negative number!")
    else:
        print("The Result is:", math.sqrt(number))

elif choice == '6':
    number = float(input("Enter a number: "))
    print("The Result is:", math.cbrt(number))

elif choice in ('1', '2', '3', '4'):
    number1 = float(input("Enter your first number: "))
    number2 = float(input("Enter your second number: "))

    if choice == '1':
        print("The Result is:", number1 + number2)
    elif choice == '2':
        print("The Result is:", number1 - number2)
    elif choice == '3':
        print("The Result is:", number1 * number2)
    elif choice == '4':
        if number2 == 0:
            print("Cannot divide by zero!")
        else:
            print("The Result is:", number1 / number2)

else:
    print("Invalid choice or mode!")
