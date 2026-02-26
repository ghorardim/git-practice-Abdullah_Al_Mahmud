from datetime import date
from utils import add, subtract, multiply, divide

# Print my name
print("Name: Abdullah Al Mahmud")

# Print today's date
today = date.today()
print("Today's date:", today)

# Use the add function from utils.py
result_add = add(5, 3)
print("5 + 3 =", result_add)

# Use the subtract function from utils.py
result_subtract = subtract(5, 3)
print("5 - 3 =", result_subtract)

# Use the multiply function from utils.py
result_multiply = multiply(5, 3)
print("5 * 3 =", result_multiply)

# Use the divide function from utils.py
result_divide = divide(5, 3)
print("5 / 3 = {:.2f}".format(result_divide))

# Add basic error handling to the calculator.
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Addition result: {:.2f}".format(add(num1, num2)))
    print("Subtraction result: {:.2f}".format(subtract(num1, num2)))
    print("Multiplication result: {:.2f}".format(multiply(num1, num2)))
    print("Division result: {:.2f}".format(divide(num1, num2)))

except ValueError:
    print("Error: Please enter valid numbers.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except Exception as e:
    print("Unexpected error:", e)