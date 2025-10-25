import csv

with open("utilities/loanApp.csv") as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')

    # print(csvReader)
    # print(list(csvReader))

    names = []
    stats = []
    for row in csvReader:
        names.append(row[0])
        stats.append(row[1])

print(names)
print(stats)

Index = names.index("Sam")
loanStatus = stats[Index]

print("The loan status is ", loanStatus)

with open('utilities/loanApp.csv', 'a') as wFile:
    # Here a stands for append, it will add at the end
    write = csv.writer(wFile)
    write.writerow(["Bob", "Rejected"])
    write.writerow(["Sam", "Approved"])
