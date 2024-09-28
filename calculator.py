import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: zero is undefined!"
    else:
        return x / y

def modulo(x, y):
    if y == 0:
        return "Error: zero is undefined!"
    else:
        return x % y

def square_root(x):
    if x < 0:
        return "Error: Square root of a negative number is undefined in real numbers!"
    else:
        return math.sqrt(x)

def get_operation():
    print("\nChoose the Number of the Opertaion to perform:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulo")
    print("6. Square Root")
    print("7. Exit")

def calculator():
    print("Welcome to the Advanced Calculator with Square Root!")
    while True:
        get_operation()
        choice = input("Enter choice (1/2/3/4/5/6/7): ")

        if choice == '7':
            print("Thank you for using the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"Result: {num1} / {num2} = {result}")
            elif choice == '5':
                result = modulo(num1, num2)
                print(f"Result: {num1} % {num2} = {result}")

        elif choice == '6':
            try:
                num = float(input("Enter number: "))
                print(f"Result: √{num} = {square_root(num)}")
            except ValueError:
                print("Invalid input! Please enter a numeric value.")

        else:
            print("Invalid choice! Please choose a valid operation.")

if __name__ == "__main__":
    calculator()

