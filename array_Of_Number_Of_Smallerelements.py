#Problem - Given an array of integers, return a new array where each element in the new array is the number of smaller elements to the right of that element in the original input array.
def myfunc(arry):
    range= len(arry)
    range_valid=range - 1
    new_lst=[]
    n=0
    while n < range_valid:
        nr=n+1
        count=0
        while nr < range:
            if arry[n] > arry[nr]:
               count += 1
            nr += 1
        new_lst.append(count)
        n += 1
    new_lst.append(0)
    return new_lst


my_lst=myfunc([3, 4, 9, 6, 1])
print (my_lst)
