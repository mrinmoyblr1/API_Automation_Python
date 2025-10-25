print("Hello")
print("Mrinmoy")
# This is new Line
a = 3
print(a)
a = 3.33
print(a)

name = "Mirnmoy"
print(name)

str = "Hello World"
print(str)

b, c, d = 5, 6.4, "Great"
print(b, c, d)

print("=====================================")
print("{}{}{}".format("Value is: ", b, " This is the values"))
print("=====================================")
print(type(b))
print(type(c))
print(type(d))

# ================================
name = "Mrinmoy"
greeting = "Hello, {}{}{}!".format(name, " ", "Biswas")
print(greeting)

print("{} I am learning {}".format("Hello", "Python"))

# ================================
name = "Mrinmoy"
age = 25
greeting = f"My name is {name} and I am {age} years old."
print(greeting)

# ================================
F_Name = "Mrinmoy"
L_Name = "Biswas"
greeting = "Hello, " + F_Name + " " + L_Name + "!"
print(greeting)

# ================================
lst = ['p', 'y', 't', 'h', 'o', 'n']
print(lst[1:2])

dct = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(dct['b'])

# ================================
a = 10
b = 10
if a == b:
    print("a is equal to b")
else:
    print("a is not equal to b")


# ================================
def checker(a, b):
    if a > b:
        print("a is larger than b")
    elif a == b:
        print("a and b are equal")
    else:
        print("b is larger than a")


checker(10, 12)

# ================================
for i in range(11, 30, 5):
    print(i)

# ================================
print("================================")


class Multiplier:
    def __init__(self, a):
        self.a = a

    def multiply(self, b=1):
        print(b * (self.a))


x = Multiplier("Hello")
x.multiply(2)

# ================================
print("================================")
x = "Mrinmoy"
print(x[:4])
