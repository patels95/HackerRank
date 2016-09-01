import fileinput

length = 10
nums = []
weights = []

for line in fileinput.input():
	data = line.split()
	if fileinput.lineno() == 1:
		length = int(data[0])
	elif fileinput.lineno() == 2:
		for d in data:
			nums.append(int(d))
	else:
		for d in data:
			weights.append(int(d))

def weightedTotal(length, nums, weights):
	total = 0
	for i in range(length):
		total += nums[i] * weights[i]
	return total

print(round(weightedTotal(length, nums, weights) / sum(weights), 1))