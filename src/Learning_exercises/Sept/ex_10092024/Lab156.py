class XYZ:
    def f1(self):
        try:
            a = int(input("Enter a number\n"))
        except Exception as e:
            print("Enter int value on a")
        else:
            print(a)
        finally:
            print("FINALLY : Any how I will be printed")


x = XYZ()
x.f1()
