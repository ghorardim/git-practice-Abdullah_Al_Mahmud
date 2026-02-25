from datetime import date
from utils import add, subtract, multiply

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