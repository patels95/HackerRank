# Problem: https://www.hackerrank.com/challenges/s10-interquartile-range

import fileinput
import statistics as stats

length = 0
nums = []
freqs = []

for line in fileinput.input():
	data = line.split()
	if fileinput.lineno() == 1:
		length = int(data[0])
	elif fileinput.lineno() == 2:
		for d in data:
			nums.append(int(d))
	else:
		for d in data:
			freqs.append(int(d))


def setDataArray(nums, freqs):
	arr = []
	for i in range(length):
			for j in range(freqs[i]):
				arr.append(nums[i])
	return arr

def isOdd(length):
	if length % 2 != 0:
		return True
	else:
		return False

def splitOddArray(nums, splitIndex):
	L = nums[:splitIndex]
	U = nums[splitIndex + 1:]
	return (L, U)

def splitEvenArray(nums, length):
	half = length // 2
	L = nums[:half]
	U = nums[half:]
	return (L, U)

S = setDataArray(nums, freqs)
S = sorted(S)
median = stats.median(S)
print(S)

if isOdd(length) == True:
	medianIndex = S.index(median)
	(lower, upper) = splitOddArray(S, medianIndex + 1)
else:
	(lower, upper) = splitEvenArray(S, len(S))

p
print(float(stats.median(upper) - stats.median(lower)))
