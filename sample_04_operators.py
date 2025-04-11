# MAIN CODE

"""Let's work with operators."""

# Arithmetic operators
# (+) Addition, (-) Subtraction, (*) Multiplication, (/) Division
a = 10 + 5  # Result: 15
b = 20 - 8  # Result: 12
c = 3 * 7   # Result: 21
d = 15 / 3  # Result: 5.0 (Division always returns float)
print(a, b, c, d)
print("\n")

# Integer division operator (//)
integer_division = 10 // 3  # Result: 3 (Truncates to nearest integer)
print(integer_division)
print("\n")

# Exponent operator (**)
power = 2 ** 3  # 2 to the power of 3 = 8
print(power)
print("\n")

# Modulo operator (%), returns division remainder
remainder = 10 % 3  # 10 divided by 3 equals 3 with remainder 1
print(remainder)
print("\n")

# Comparison operators
# (==) Equal to, (!=) Not equal to, (>) Greater than, (<) Less than,
# (<=) Less than or equal to, (>=) Greater than or equal to
equal = (5 == 5)        # True
print(equal)
not_equal = (4 != 2)    # True
print(not_equal)
greater = (6 > 3)       # True
print(greater)
less = (5 < 10)         # True
print(less)
less_equal = (7 <= 7)   # True
print(less_equal)
greater_equal = (8 >= 6)  # True
print(greater_equal)
print("\n")

# Logical operators (and, or, not)
# Combine boolean values
logical_and = (True and False)  # False (both must be True)
print(logical_and)
logical_or = (True or False)     # True (at least one True)
print(logical_or)
logical_not = not True           # False (inverts the value)
print(logical_not)
print("\n")

# Assignment operators (=, +=, -=)
x = 10    # Basic assignment
print(x)
x += 5    # Equivalent to x = x + 5 → 15
print(x)
x -= 3    # Equivalent to x = x - 3 → 12     # 12
print(x)
print("\n")

# Membership operators (in, not in)
my_list = [1, 2, 3]
is_in = 2 in my_list       # True
print(is_in)
not_in = 4 not in my_list  # True
print(not_in)
print("\n")

# Identity operators (is, is not)
# Compare if two variables are the same object
num1 = 5
num2 = 5

# True (for small integers, Python reuses objects)
same_object = num1 is num2
print(same_object)
print("\n")

# False (different objects)
not_same_object = num1 is not num2
print(not_same_object)
