def check_index(lst,user_input):
    # find index of element from our list
    if user_input in lst:
        return lst.index(user_input)
    
    return f'the element doesn''t exits'



user_input=int(input("enter number from array to find index:"))
array=[10,20,30,40]
result=check_index(array,user_input)


print(result)