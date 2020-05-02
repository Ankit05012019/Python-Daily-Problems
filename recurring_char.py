def recurringChar(str):
    cher=''

    for i in str:
        num=0
        char=i
        for j in str:
            if j == char:
               num += 1
               if num == 2:
                   return f"{j} recurred "
               else:
                   continue

ans=recurringChar('acbbac')
print (ans)

def recurringChar2(str):

 n = len(str)
 s=0
 while n > s:
    sp=s+1
    while n > sp:
        if str[s] == str[sp]:
           return f"{str[s]} is recurring"

        else:
           sp += 1
    s += 1


def recurred(str):
    n = len(str)
    s = 0
    while n > s:
        if str[s] == str[s+1]:
           print (f"{str[s]} recurred")
           break
        else:
           s += 1

mychar=recurringChar2('acbbac')
print (mychar)
recurred('acbbac')
