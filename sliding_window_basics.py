arr = [2, 1, 5, 1, 3, 2]
k=3

i=0
j=0

n=len(arr)
sum1=0
result=0

while (j<n):
    sum1 += arr[j]
    
    if (j - i + 1 < k):
        j += 1
    
    elif (j - i + 1 == k):
        result = max(sum1, result)
        
        sum1 -= arr[i]
        i += 1
        j += 1 
print(result)
        
        