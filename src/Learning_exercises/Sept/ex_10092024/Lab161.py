import os

full_path_file = os.path.join(r"C:\Users\USER\PycharmProjects\pythonProject\src\Learning_exercises\Sept\ex_10092024",
                              "thamim.txt")

file = open(full_path_file, 'r')
content = file.read()
print(content)
