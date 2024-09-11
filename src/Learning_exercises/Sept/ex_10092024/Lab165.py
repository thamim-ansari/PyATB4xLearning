import csv

with open(r'C:\Users\USER\PycharmProjects\pythonProject\src\Learning_exercises\Sept\ex_10092024\ TestData.csv') as csvfile:
    reader = csv.reader(csvfile)
    for col in reader:
        print(col[0], col[1], sep="|")
