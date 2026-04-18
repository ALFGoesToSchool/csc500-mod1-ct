# CSC500 Module 1 Critical Thinking Assignment - Part 2
# Author: Andy
# Description: Program to find the multiplication and division of two numbers.

def main():
    # Prompt the user to input two numbers
    num1 = float(input("Enter the first number (num1): "))
    num2 = float(input("Enter the second number (num2): "))

    # Perform multiplication
    multiplication_result = num1 * num2

    # Display results
    print("\n----- Results -----")
    print(f"Multiplication: {num1} * {num2} = {multiplication_result}")

    # Perform division, guarding against division by zero
    if num2 != 0:
        division_result = num1 / num2
        print(f"Division:       {num1} / {num2} = {division_result}")
    else:
        print("Division:       Cannot divide by zero.")


if __name__ == "__main__":
    main()
