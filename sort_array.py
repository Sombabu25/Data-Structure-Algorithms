# sort the given array in ascending order


array=[4,6,32,65,2,7,8]

'''
array.sort()
print(array)
              '''


# using selection sort

n = len(array)

for i in range(n):
    for j in range(i+1):
        if array[i] < array[j]:
           temp = array[i]
           array[i] = array[j]
           array[j] = temp



print(array)
