# Task 3


# -Explain the difference between the = operator and the == operator in Python.

"""In Python, a single equals sign (=) is known as the assignment operator, which is used to assign values to a
variable. On the other hand, a double equals sign (==) is called the equality operator, and it is used to check
if two values are equal"""

# Assignment operator(=):
a = 10
a = a + 10
print(a)  # output 20
# Equality Operator(==):
a = 10
b = 20
print(a == b)  # a is not equal to b.so, it will give False


# - What does the ** operator do in Python, and how is it used?
"""In Python, the ** operator is used for exponentiation. It raises a number to the power of another number."""
# Example:
a = 2
b = 3
print(a**b)  # which gives cube of 2 which is 2 power of 3 = 8
print(b**a)  # which gives square of 3 which is 3 power of 2 = 9

# -What does the ^ operator do in Python, and in what context is it commonly used?
"""In Python, the ^ operator is the bitwise XOR (exclusive OR) operator. It performs a bitwise exclusive OR 
operation on two integers, which means it compares the bits of the numbers and returns a new integer where 
each bit is set to 1 if the corresponding bits of the operands are different, and 0 if they are the same."""
# Example Swapping Numbers:
a = 5
b = 3
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)  # output: 3 5
