import sys

file1 = sys.argv[1]
# file1 = 'nums.txt'
with open(file1) as file:
    nums = ([line.rstrip() for line in file])

step = 0
nums_result = [int(i) for i in nums]

avarage = round(sum(nums_result) / len(nums_result))

for index, i in enumerate(nums):
    i = int(i)
    while i != avarage:
        if i < avarage:
            i += 1
            step += 1
        elif i > avarage:
            i -= 1
            step += 1
        else:
           nums[index] = i

print(step)