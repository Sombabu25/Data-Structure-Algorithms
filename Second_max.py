a = [-3, -9, -5, -2, -10, -8, -11]
max1 = float('-inf')
second_max = float('-inf')
for i in range(len(a)):
    if a[i] > max1:
        second_max = max1
        max1 = a[i]

    elif  a[i] < max1 and a[i] > second_max:
        second_max = a[i]

print(second_max)
    
