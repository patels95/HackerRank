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

nums = sorted(nums)
median = stats.median(nums)

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

if isOdd(length) == True:
	medianIndex = nums.index(median)
	(lower, upper) = splitOddArray(nums, medianIndex)
else:
	(lower, upper) = splitEvenArray(nums, length)

print(int(stats.median(lower)))
print(int(median))
print(int(stats.median(upper)))
