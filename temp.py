array2=[3,10,20,30,40,50]
'''
array3= array2.copy()

print(array2)
print(array3)


array3=array2[:]
print(array3)    '''

array3=[]
# array3=list(array2)
# array3.reverse()

# print(array2)
# print(array3)

# for i in array2:
#     if i %2 != 0:
#         array3.append(i)

# print(array3)



# n=10

# a=0
# b=1

# fibo = [a,b]


# for i in range(n-2):
#     c = a+b
#     fibo.append(c)
#     a = b
#     b = c

# print(fibo)

u=0
l=0
n=0
s=0



upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

lower = "abcdefghijklmnopqrstuvwxyz"

number = "0123456789"

symbol = "!@#$%^&*()_-{[]}<>?/."


password = "######@@@123sR"

if len(password) >= 6:
    for i in password:
        if i in upper:
            u += 1

        if i in lower:
            l += 1
        if i in number:
            n  += 1
        if i in symbol:
            s += 1
    if u and l and n and s:
        print("strong password")
    else:
        print("weak password")

else:
    print("weak password")