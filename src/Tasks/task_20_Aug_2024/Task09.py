# Task 9

# Write a program that prints numbers from 1 to 100. # Loop For

# However, for multiples of 3, print "Fizz" instead of the number, and

# for multiples of 5, print "Buzz."

# For numbers that are multiples of both 3 and 5, print "FizzBuzz."

for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("Fizz Buzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
