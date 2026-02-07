#Task1
try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    result = numerator / denominator
    print(f"The result of {numerator} divided by {denominator} is: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed. Please provide a non-zero denominator.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values for numerator and denominator.")
finally:
    print("Operation completed.")