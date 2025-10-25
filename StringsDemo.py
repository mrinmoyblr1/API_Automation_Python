str1 = "RahulShettyAcademy.com"
str2 = "Consulting Firm"
str3 = "RahulShetty"

print(str1[1])
print(str1[0:5])  # Sub-String in python
print(str1 + str2)  # String concatenation in Python
print(str3 in str1)
# Sub-String check in python
# #It wll return true/false

var = str1.split(".")  # Split in python
print(var)
print(var[0])

# trim extra space in python
str4 = "   great    "
print(str4)
print(str4.strip())  # to remove extra space
print(str4.lstrip())  # to remove extra space at the left side
print(str4.rstrip())  # to remove extra space at the left side

