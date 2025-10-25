file = open("test.txt")

# Read all the contents of file
# Read nth number of characters
# print(file.read(2))
# print("=======")
# print(file.read())
# print("=======")
# file.close()
# file = open("test.txt")
# print("File Reopen")

# Read one single line using readLine()
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

# Print line by line using readLine method
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

# ===============================
# Use readline() to get all the content into List
for line in file.readlines():
    print(line)

file.close()
