# Simple Calculator in Python
# Features: Addition, Subtraction, Multiplication, Division

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Main program
print("===== Simple Calculator =====")

# Input two numbers
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
except ValueError:
    print("Invalid input! Please enter numbers only.")
    exit()

# Choose operation
print("\nSelect operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter choice (1/2/3/4): ")

# Perform calculation
if choice == '1':
    result = add(num1, num2)
    operator = '+'
elif choice == '2':
    result = subtract(num1, num2)
    operator = '-'
elif choice == '3':
    result = multiply(num1, num2)
    operator = '*'
elif choice == '4':
    result = divide(num1, num2)
    operator = '/'
else:
    print("Invalid choice!")
    exit()

# Display result
print(f"\nResult: {num1} {operator} {num2} = {result}")
