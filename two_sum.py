# nums = [10,20,5,30]

# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i] + nums[j] == target:
#            return [i, j]


# hash map  for constacnt lookup O(1) time for insert, delete, find element

nums = [10,20,5,30]

d = {}
target = 25

for index, value in enumerate(nums):
    diff = target - value

    if diff in nums:
       d[diff] = index
       




