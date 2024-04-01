import os
# f = open("python\chapter-7\demo.txt","r")

# print(f.read())

# f.close()


f = open("python\chapter-7\sample.txt", "w")

f.close()


with open("python\chapter-7\sample.txt", "w") as f:
    f.write("Hello World")

os.remove("python\chapter-7\sample.txt")