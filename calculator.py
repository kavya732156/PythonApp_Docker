# Simple Calculator in Python

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def main():
    print("=== Simple Calculator ===")
    print("Operations: +  -  *  /")
    
    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operation (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if op == '+':
                result = add(num1, num2)
            elif op == '-':
                result = subtract(num1, num2)
            elif op == '*':
                result = multiply(num1, num2)
            elif op == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operation!")
                continue

            print(f"Result: {result}")

            choice = input("Do another calculation? (y/n): ").lower()
            if choice != 'y':
                print("Goodbye!")
                break

        except ValueError:
            print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    main()

