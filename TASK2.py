# Simple Calculator

# Prompt user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Select operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter choice (1/2/3/4): ")

# Perform calculation based on user choice
if choice == '1' or choice == '+':
    result = num1 + num2
    operation = '+'
elif choice == '2' or choice == '-':
    result = num1 - num2
    operation = '-'
elif choice == '3' or choice == '*':
    result = num1 * num2
    operation = '*'
elif choice == '4' or choice == '/':
    if num2 != 0:
        result = num1 / num2
        operation = '/'
    else:
        print("Error: Division by zero is not allowed.")
        exit()
else:
    print("Invalid input. Please select a valid operation.")
    exit()

# Display the result
print(f"{num1} {operation} {num2} = {result}")
