import fileinput
import statistics as stats
import collections

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
median = stats.median(nums)


def calculateMode(nums):
	# key = item in nums, value = count of item
	countDict = {}
	for n in nums:
		if n in countDict:
			count = countDict[n]
			countDict[n] = count + 1
		else:
			countDict[n] = 1

	# ordered dictionary
	od = collections.OrderedDict(sorted(countDict.items()))
	key = 0
	maxCount = 0
	for k, v in od.items():
		if v > maxCount:
			maxCount = v
			key = k

	return key

print(mean)
print(median)
print(calculateMode(nums))