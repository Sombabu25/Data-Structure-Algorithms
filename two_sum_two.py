arr = [1,2,3,4,2]

h  = set()
prev = 1
for i in arr:
    
    if i not in h:
       h.add(i)
       prev = i
    
print(prev)