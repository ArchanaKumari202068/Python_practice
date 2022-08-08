

# d = {"name":["archana","Ishika"],"sem":5, 
# "Roll":202068,"CSE":True,34:{"age:19"}}
# print(d)
# for i in d.keys():
#     print(d[i])

# print(type(d))

# print(d.keys())

# print(d.values())
# print(d["name"])
# print(type(d["name"]))
# print(d[34]["age"])    --- error how to access 19

# d[True] ="computer"
# print(d["name"][1] + " "+ "hello")
# print(d)
# d.update({"CSE": "B.tech"})
# print(d)
# del d["name"][0]
# print(d)
# del d
# print(d)
# d.clear()
# print(d)

def number_num(n):
    if(n%2==0):
        return True

    return False   
def printing(num):
    val = number_num(num)
    if (val==True):
      print("even no.")
    else:
        print("num is odd")  

number =int(input())       
printing(number)      