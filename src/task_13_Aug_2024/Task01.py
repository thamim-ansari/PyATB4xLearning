''' Create a program that takes a number as user input and prints a multiplication table.
f"{}" String format concept
User input - num int -> 10, 100, -1, 2, 3.14 -> input
9x1 = 9
9x2 = 18... till 10 '''

num = input("Enter a number: ")

if(num.isdigit()):
   num = int(num)
else:
    num = float(num)

print("Table of ",num)
print(f"{num}*1 = {num}")
print(f"{num}*2 = {num*2}")
print(f"{num}*4 = {num*4}")
print(f"{num}*5 = {num*5}")
print(f"{num}*6 = {num*6}")
print(f"{num}*3 = {num*3}")
print(f"{num}*7 = {num*7}")
print(f"{num}*8 = {num*8}")
print(f"{num}*9 = {num*9}")
print(f"{num}*10 = {num*10}")