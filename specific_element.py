def check_specific(lst,user_input):
    # check user input  is presented in our list
    if user_input in lst:
        return True
    
    return False



user_input=int(input("enter any number to check:"))
array=[10,20,30,40]
result=check_specific(array,user_input)


print(result)
