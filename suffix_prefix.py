# arr = [1,2,3,4]
# r = []
# prefix = 1
# for i in range(len(arr)):
#     prefix *= arr[i]
#     r.append(prefix)

    

# print(r)


# arr = [1,3,9,21]
# s = []
# suffix = 1

# for j in range(len(arr)-2, -1, -1):
#     suffix *= arr[j]
#     print(suffix)
    # s.append(suffix)

# print(s)

'''
PREFIX Calculation
Rule:
prefix[i] = product of all elements before index i
'''
# arr = [1,2,3,4]
# n = len(arr)
# r = [arr[0]]

# product = 1
# for i in range(1, n):
#     product *=  arr[i]
#     r.append(product)
# print(r)


# arr = [1,2,3,4]
# n = len(arr)
# s = [1] * n
# # product = 1
# for i in range(len(arr)-2, -1, -1):
#     s[i] *= arr[i]
#     product = s[i] * arr[i+1]
#     s.append(product)
# print(s)


arr = [1,2,3,4]
n = len(arr)

result = [1] * n

# prefix pass
prefix = 1
for i in range(n):
    result[i] = prefix
    prefix *= arr[i]

suffix = 1
for i in range(n-1, -1, -1):
    result[i] *= suffix
    suffix *= arr[i]

print(result)





