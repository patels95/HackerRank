
import fileinput

n = 0
k = 0
c = []
b = 0

# read input
for line in fileinput.input():
    data = line.split()
    if fileinput.lineno() == 1:
        n = int(data[0])
        k = int(data[1])
    elif fileinput.lineno() == 2:
        for d in data:
            c.append(int(d))
    else:
        b = int(data[0])


def calculateTotal(c):
    sum = 0
    for num in c:
        sum += num
    return sum / 2

def calculateAdjustedTotal(c, k):
    sum = 0
    for i in range(len(c)):
        if i != k:
            sum += c[i]
    return sum / 2


total = calculateTotal(c)
adjustedTotal = calculateAdjustedTotal(c, k)

if adjustedTotal == b:
    print("Bon Appetit")
else:
    print(int(total - adjustedTotal))



