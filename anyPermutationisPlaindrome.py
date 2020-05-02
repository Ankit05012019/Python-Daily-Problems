#Given a string, determine whether any permutation of it is a palindrome.
from itertools import permutations

def permutation(str):

    perm = permutations(str)
    for s in perm:
        new_str =''.join(s)
        if new_str == new_str[::-1]:
           print ("palindrome")
           break
    else:
        print ("not plaindrome")


permutation('carrace')

lst=['a','b','c']
print("".join(lst))



def pigeonhole(lst):

    max_val=max(lst)   #max value from the input array
    min_val=min(lst)   # min vlaue from the input array
    len=max_val - min_val + 1  # range
    pg=[0] * len
    for i in lst:
        if pg[i - min_val] != i:
           pg[i - min_val] = i
        else:
           return f"{i} is the duplicate value"
    print("no duplicates found")


result=pigeonhole([3,4,6,6,7])
print(result)
