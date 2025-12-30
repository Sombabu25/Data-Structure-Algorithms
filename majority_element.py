from collections import Counter

a = [2,2,1,1,1,2,2]
b = Counter(a)
print(b)
r = 0
for key,value in b.items():
    print(key,value)
    if value > r:
        r = value
        c = key


    # if b[i] > r:
    #     r = i
    # print(b[i])

# for i in b:
#     if b[i] > r:
#         r = a
print(c)