import math
def calculate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '**':
        return math.pow(num1, num2)
    elif operator == 'square':
        return num1 * num1
    elif operator == 'sqrt':
        if num1 >= 0:
            return math.sqrt(num1)
        else:
            return "Error: Cannot take square root of negative number"
    elif operator == 'cube':
        return num1 * num1 * num1
    elif operator == 'cbrt':
        if num1 >= 0:
            return num1 ** (1/3)
        else:
            return -(-num1) ** (1/3)
    elif operator == 'log':
        if num1 > 0:
            return math.log(num1)
        else:
            return "Error: Logarithm undefined for non-positive numbers"
    elif operator == 'log10':
        if num1 > 0:
            return math.log10(num1)
        else:
            return "Error: Logarithm undefined for non-positive numbers"
    elif operator == 'inverse':
        if num1 != 0:
            return 1 / num1
        else:
            return "Error: Division by zero"
    elif operator == 'sin': # Sine function
        return math.sin(math.radians(num1)) # Convert degrees to radians
    elif operator == 'cos':# Cosine function
        return math.cos(math.radians(num1)) # Convert degrees to radians
    elif operator == 'tan': # Tangent function
        return math.tan(math.radians(num1)) # Convert degrees to radians     
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"
    
while True:
    operator = input('Enter operator (+, -, *, /, **, square, sqrt, cube, cbrt, inverse, sin, cos, tan, log, log10): ') # Ask user for operator
    
    if operator in ['square', 'sqrt', 'cube', 'cbrt', 'inverse', 'sin', 'cos', 'tan' 'log', 'log10']: # Check if operator is unary
        num1 = float(input("Enter number: "))
        result = calculate(num1, operator, None)
        print(result)

    elif operator in ['+', '-', '*', '/', '**']: # Check if operator is binary
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /, **): ")
        num2 = float(input("Enter second number: "))
        result = calculate(num1, operator, num2)
        print(result)

    choice = input("Do you want to continue? (yes/no): ").lower() # Ask user if they want to continue
    if choice == 'yes':
        continue
    elif choice == 'no':
        print("Goodbye!")
        break
    else:
        print("Please enter 'yes' or 'no'.")