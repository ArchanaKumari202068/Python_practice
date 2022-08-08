

def length(ls):
    count=0
    for i in ls:
        count+=1
    return count


# ls = [1,3,5,56,86,23,898,0,27,90]    
# for i in range(length(ls)):
#     print(ls[i])

ls = [1,3,5,56,86,23,898,0,27,90]   
print(length(ls))
ls = [1,3,5,56,86,23,898,0,27,90,100]  
ls.remove(3)
print(max(ls))


