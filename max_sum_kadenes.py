a = [-2, 7, -3, 4]

curr_sum = 0
max_sum =  float("-inf")

for i in a:
    curr_sum = curr_sum + i

    if curr_sum > max_sum:
        max_sum = curr_sum 
    

    if curr_sum < 0:
        curr_sum = 0

print(max_sum)