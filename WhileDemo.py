it = 10

while it > 1:
    if it == 9:
        it = it - 1
        continue
    if it == 3:
        break;
    print(it)
    it = it - 1

print("While Loop execution is done")

# ==================================================
for i in range(11, 20, 6):
    print(i)


# % python3 WhileDemo.py
# 11
# 17


# ==================================================

class Multiplier:
    def __init__(self, a):
        self.a = a

    def multiply(self, b=1):
        print(b * (self.a))


x = Multiplier("Hello")
x.multiply(2)
# % python3 WhileDemo.py
# 'HelloHello'

# ==================================================
