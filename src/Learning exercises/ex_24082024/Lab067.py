# User Defined
# 1. The can't return -> non return
# 2.They can return something
# They have parameters
# They don't parameters / arguments


# 1. The can't return -> non return
# # No Return Type and No Parameter / Argument - NRNP
def greet():
    print("Hello World")


result = greet()
print(result)


# 2. # No Return Type and with Argument
def greet_by_name(name):
    print("Hello,", name)


greet_by_name("thamim")


# # 3. No Return Type and with Default Argument
def say_hello_default_arg(name="thamim"):
    print("Hello", name.upper())


say_hello_default_arg("ansari")
say_hello_default_arg()
say_hello_default_arg(name="ram")  # positional argument


def multiple_args(name1="lokesh", name2="thamim", name3="faizal"):
    print("Multiple Arguments", name1, name2, name3)


multiple_args(name1="Ram", name2="Yunus", name3="Deepshikha")
multiple_args(name1="THAMIM")


# 4. Argument + return Type
def sum_of_two_number(num1, num2):
    return num1 + num2


def sum_of_two_number_with_default(num1=100, num2=200):
    return num1 + num2


# result = sum_of_two_number(10, 34)
result = sum_of_two_number(num1=34, num2=34)
result = sum_of_two_number_with_default()
print(result)