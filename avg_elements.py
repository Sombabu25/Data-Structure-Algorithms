# find avg of all elements in an array

array=[10,20,30,40,50]

sum_of_elements=0
number_of_elements=len(array)


for i in array:
    sum_of_elements += i


avg = sum_of_elements // number_of_elements

print(f'average of all elements: {avg}')