nums = [1,4,4]
target = 7
# p = nums[0]
# r = []

r = [nums[0]]

for i  in range(1,len(nums)):
    prefix_sum = nums[i] + nums[i-1] + nums[0]
    r.append(prefix_sum)

print(prefix_sum)

    # if prefix_sum == target:
    #    r.append(i)
    #    r.append(i-1)
    # if nums[i] == target:
    #     r.append(nums[i])

            
print(r)