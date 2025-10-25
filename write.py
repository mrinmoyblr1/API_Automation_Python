# file = open("test.txt")
# file.close()

# Read the file and store all the lines in list
# Reverse the list
# Write back the reversed list to the file
# To open any file as below
# w is for write mode
# r for Read-Only mode
# Use readline() to get all the content into List

with open("test.txt", "r") as reader:
    # In case of this step we do not need to to file.close()
    # #It will open the file in Read Mode only as we used "r"
    content = reader.readlines()  # It will read all the lines one by one
    # reversed(content)  #This will reverse the List

# for i in reversed(content):
#     print(i)

# Write back the reversed list to the file
with open("test.txt", "w") as writer:
    for line in reversed(content):
        writer.write(line)
