# Task 11

# Fibonaci series 0,0+1, 0+1+1, n = 7 0, 1, 2, 3, 5, 8, 13

f = int(input("Entre the number: "))
a = 0
b = 1
fib = 0
fibonacci_series_list = ["0"]
if f == 0:
    print(0)
elif f == 1:
    print("0,1")
else:
    for i in range(2, f + 1):
        fib = a + b
        a = b
        b = fib
        fibonacci_series_list.append(str(fib))
    print(",".join(fibonacci_series_list))
