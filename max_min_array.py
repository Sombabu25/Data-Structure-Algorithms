# find max and min from an array

array=[4,6,32,65,2,7,8]

'''
print(f'maximum: {max(array)}' )
print(f'minimum: {min(array)}')   
 
 '''

max_element = array[0]
min_element = array[0]

for i in array:
    if max_element < i:
        max_element = i
    
    elif min_element > i:
         min_element = i


print(max_element)
print(min_element)
