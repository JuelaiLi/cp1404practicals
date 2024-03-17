"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A ValueError will occur if the user enters a value that cannot be converted to an integer using int() in the lines:
numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))
For example, entering a non-numeric string.

2. When will a ZeroDivisionError occur?
A ZeroDivisionError will occur if the user enters 0 as the denominator in the line:
fraction = numerator / denominator

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
To avoid the possibility of a ZeroDivisionError, we can add a conditional check before performing the division to ensure that the denominator is not zero.
"""
# Original code:
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# Here's the modified code:
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == 0:
        raise ValueError("Denominator cannot be zero!")

    fraction = numerator / denominator
    print(fraction)

except ValueError as ve:
    print(f"Error: {ve}")
except ZeroDivisionError:
    print("Cannot divide by zero!")

print("Finished.")
