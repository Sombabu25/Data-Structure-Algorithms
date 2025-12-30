# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None



# Node1 = Node(10) 
# Node2 = Node(20)
# Node3 = Node(30)
# Node4 = Node(40)

# Node1.next = Node2
# Node2.next = Node3
# Node3.next = Node4


# head = Node1

# while head:
#     print(head.data, end="->")
#     head = head.next
# print("None")


# palindrome number - >  121,  

# num = 121

# temp = 121
# reverse = 0

# while num != 0:
#     digit =  num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# if reverse == temp:
#     print("palindrome")
# else:
#     print("not palindrome")



# range 10  - 130

# r = []
# s = []
# for i in range(10,21):
#     if i % 2 == 0:
#         r.append(i)
#     else:
#         s.append(i)

# print(f'evens list: {r}')
# print(f'odds list: {s}')

r = []
for i in range(10, 130):
     if str(i) == str(i)[::-1]:
          r.append(i)
print(r)
