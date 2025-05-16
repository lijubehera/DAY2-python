# Variables and Data Types
a = 30          # Integer
b = "Harry"     # String
c = 71.22       # Float

print(type(a))  # <class 'int'>
print(type(b))  # <class 'str'>
print(type(c))  # <class 'float'>

# Rules for defining variable names
harry_one = 1
_one2 = 2
# 2cool = 5  ❌ Invalid: can't start with digit
# my name = "hello" ❌ Invalid: no spaces allowed

# Operators
x = 10
y = 3

# Arithmetic Operators
print("Addition:", x + y)
print("Division:", x / y)
print("Modulus:", x % y)

# Assignment Operator
x += 5
print("x after x += 5:", x)

# Comparison Operators
print("Is x > y?", x > y)

# Logical Operators
print("Logical AND:", (x > 5 and y < 5))

# Typecasting
num_str = "31"
num_int = int(num_str)
num_float = float(num_int)

print("String to Integer:", num_int)
print("Integer to Float:", num_float)
print("Integer to String:", str(num_int))

# Input function
user_input = input("Enter your name or age: ")
print("You entered:", user_input)
print("Data type of input:", type(user_input))

# Typecast if expecting number
age = input("Enter your age: ")
age = int(age)  # Convert to integer
print("Age after conversion:", age)
print("Type of age:", type(age))
