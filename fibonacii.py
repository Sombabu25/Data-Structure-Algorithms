# first n fibo sequence

n=10

a=0
b=1

fibo = [a,b]


for i in range(n-2):
    c = a+b
    fibo.append(c)
    a = b
    b = c

print(fibo)
