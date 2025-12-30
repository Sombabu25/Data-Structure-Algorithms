nums = [1,4,4]
sum1 = nums[0]
prefix_sum = nums[0]

r = [nums[0]]

for i  in range(1,len(nums)):
    prefix_sum = nums[i-1] + nums[i] 

    # sum1 += nums[i]
    # r.append(sum1)
print(prefix_sum)

# print(sum1)
print(r)