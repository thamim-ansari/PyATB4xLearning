# Task 10
# Factorial n = 5 5! -->54321 -> 120
# 3! -> 321 -> 6
# 4! -> 432*1 -> 24


num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print(f"Factorial of {num} is {factorial}")
