


lst=[2,3,4,5,6,8,7,9]
first_index=lst[0]
last_index=lst[-1]

'''
lst.remove(first_index)
lst.remove(last_index)  '''

n=len(lst)
output=[]
for i in range(1,n-1):
    output.append(lst[i])
    

print(output)
