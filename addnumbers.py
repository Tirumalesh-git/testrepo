def add_numbers(num1, num2):
    """Add two numbers and return the result."""
    return num1 + num2

def main():
    # Get user input
    try:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        
        # Call the add function
        result = add_numbers(number1, number2)
        
        # Display the result
        print(f"The sum of {number1} and {number2} is: {result}")
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
