
#copy one array to another  and change to copied array shouldn't reflect in another
array2=[10,20,30,40,50]
'''
array3= array2.copy()

print(array2)
print(array3)


array3=array2[:]
print(array3)    '''


array3=list(array2)
array3.reverse()

print(array2)
print(array3)
