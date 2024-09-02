# Class and Object Assignment

"""Create a Employee Class
A - name,age, phone, address, eid
B - walk, talk, printdetails,
with the Constructor which will set the values
Ask the user about the information for E1, E2
print the details of the E1, E2 via the print employee functions."""


class Employee:
    eid = None
    name = None
    age = None
    address = None
    phone = None
    gender = None

    def __init__(self, eid, name, age, address, phone, gender):
        self.eid = eid
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.gender = gender

    def walk(self):
        print(self.name, "can walk")

    def talk(self):
        print(self.name, "can talk")

    def print_details(self):
        him_or_her = "him" if self.gender == "male" else "her"
        print("-----------------------------")
        self.walk()
        self.talk()
        print(
            f"eid {self.eid} refers to {self.name}.\n{self.name} is {self.age} years old.\nCurrently living in {self.address}.\nyou can contact {him_or_her} through {self.phone} this mobile number.")


emp1 = Employee(1, "Raj", 25, "bangalore", 8989898990, "male")
emp1.print_details()

emp1 = Employee(2, "Rani", 30, "chennai", 88998988990, "female")
emp1.print_details()
