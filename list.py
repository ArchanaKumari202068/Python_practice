# ls = ["name",True,66.7,23]
# print(ls)
# ls = ["name",[True,66.7],23]
# print(ls)
# print(type(ls))
# indexing start from 0 and -1 from last in list
"""
ls =    ["A","B","c","D","E"]
indexing  -5    -4    -3     -2   -1
print(ls[2])

"""

# ls=[True,"A","B",51,"C","D","E",False]
# print(ls[3], ls[-4])

# print(ls[-2])
# ls=[True,"A","B",51,"C","D","E",False]
# print(ls)
# ls[-5]="50"
# print(ls)

# ls=[True,"A","B",51,"C","D","E",False]
# ls.append('list')
# print(ls)
#delete
# ls=[True,"A","B",51,"C","D","E",False]
# del(ls[-5])
# print(ls)


# ls=[True,"A","B",51,"C","D","E",False]
# print(ls[3:])
# print(ls[:6])
# print(ls[:])

# ls=[1,322,5,0,10,4,89,76,67,66]
# for i in range(len(ls)):
#     print(ls[i])


#ls=[1,322,5,0,10,4,89,76,67,66]
# maximum = -1
# for i in ls:
#     if maximum < i:
#         maximum = i

# print(maximum)
# print(max(ls))




# error
# ls=[1,322,5,0,10,4,89,76,67,66]
# minimum = list[0]
# for i in ls:
#     if minimum >i:
#         minimum = i

# print(minimum)
# print(min(ls))

# ls=[1,322,5,0,10,4,89,76,67,66]
# for i in ls:
#     print(ls)

# error
# ls=[1,322,5,0,10,4,89,76,67,66]
# for i in ls:
#     if i<ls:
#      print(i)

ls=[1,322,5,0,10,4,89,76,67,66]
count=0

for i in ls:
    count+=1
    print("hello world ")

print(count)