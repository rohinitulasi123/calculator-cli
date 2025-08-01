# Step 1: Define the function for addition
def add(a, b):
    return a + b

# Step 2: Define the function for subtraction
def subtract(a, b):
    return a - b

# Step 3: Define the function for multiplication
def multiply(a, b):
    return a * b

# Step 4: Define the function for division
def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

# Step 5: Show calculator menu
def show_menu():
    print("\n===== Simple Calculator =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

# Step 6: Main calculator function
def calculator():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        # Step 7: Check for exit option
        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        # Step 8: Validate the choice
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please try again.")
            continue

        # Step 9: Take numeric input from user
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        # Step 10: Perform calculation based on user choice
        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)

        print("Result:", result)

# Step 11: Entry point of the program
if __name__ == "__main__":
    calculator()
