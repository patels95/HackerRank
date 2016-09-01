# Problem: https://www.hackerrank.com/challenges/s10-standard-deviation

import fileinput
import statistics as stats

length = 0
nums = []

for line in fileinput.input():
	data = line.split()
	if fileinput.lineno() == 1:
		length = int(data[0])
	else:
		for d in data:
			nums.append(int(d))

mean = stats.mean(nums)

def squaredDistance(nums):
	arr = []
	for n in nums:
		arr.append((n - mean) ** 2)
	return arr

def calculateStdDev(total, length):
	return (total / length) ** 0.5


dist = squaredDistance(nums)

print(round(calculateStdDev(sum(dist), length), 1))