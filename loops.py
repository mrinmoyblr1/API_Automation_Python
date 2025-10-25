greeting = "Good Morning"
a = 4

if greeting == "Morning":
    print("Condition Matches")
    print("Second Line")
else:
    print("Condition do not match")
print("if else statement")

if a > 2:
    print("Condition matches")
else:
    print("Condition not match")



# for loop
obj = [2, 3, 4, 7, 9]
for i in obj:
    if i > 2:
        print(i)
        print("Condition matches....")

for i in obj:
    print(i * 2)



# Sum of first 5 natural number ? 1+2+3+4+5=15
for j in range(1, 6):
    print(j)

sumOfNumbers = 0
for j in range(1, 6):
    sumOfNumbers = sumOfNumbers + j
print(sumOfNumbers)

for k in range(1, 10, 2):
    print(k)
print("Skipping First Index.....")
for m in range(10):
    print(m)
