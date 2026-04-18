# CSC500 Module 1 Critical Thinking Assignment - Part 1
# Author: Andy
# Description: Program to find the addition and subtraction of two numbers.

def main():
    # Prompt the user to input two numbers
    num1 = float(input("Enter the first number (num1): "))
    num2 = float(input("Enter the second number (num2): "))

    # Perform addition
    addition_result = num1 + num2

    # Perform subtraction
    subtraction_result = num1 - num2

    # Display the results
    print("\n----- Results -----")
    print(f"Addition:    {num1} + {num2} = {addition_result}")
    print(f"Subtraction: {num1} - {num2} = {subtraction_result}")


if __name__ == "__main__":
    main()
