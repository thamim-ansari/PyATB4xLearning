'''
Create a program , take 2 inputs from the user num1, num2 and give them
max
pow num1 to num2
sub, mul, sum, div.
Format your out with f{""}
'''

num1 = int(input('Enter a number for num1: '))
num2 = int(input('Enter a number for num2: '))

#print maximum number of num1 and num2
print(f"Maximum number of {num1} and {num2} is {max(num1, num2)}")

#print pow of num1 to num2
print(f"power of num1 to num2 is: {pow(num1, num2)}")

# print Addition
print(f"Addition of {num1} and {num2} is {num1+num2}")
# print Subtraction
print(f"Subtraction of {num1} and {num2} is {num1-num2}")
# print Multiplication
print(f"Multiplication of {num1} and {num2} is {num1*num2}")
# print Division and use format f{""}
print(f"Division of {num1} and {num2} is {num1/num2:.2f}")


