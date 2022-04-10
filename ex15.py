from sys import argv

script, filename = argv

print(f"we are going to erease {filename}.")
print("if you dont want that, hit ctrl-c.")
print("if you do want that, hit return")

input("?")

print("opening the file..")
target = open(filename, 'a+')

print("truncating the file. goodbye")
target.truncate()

print("now im going to ask you for three lines")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("im going to write these to the file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("and finally,we close it")
target.close()
