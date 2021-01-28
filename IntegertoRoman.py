"""Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer.
Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.
Example:
solution(1000) # should return 'M'
Help:
Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
Remember that there can't be more than 3 identical symbols in a row.
More about roman numerals - http://en.wikipedia.org/wiki/Roman_numerals"""


irmap = {1:'I', 2: 'II' , 3:'III', 4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',10:'X',50:'L',100:'C',500:'D',1000:'M'}
values =[1,5,10,50,100,500,1000]

def convertI2R(num):
    for i in range(10,50):
        if i not in values:
           digits=[]
           s=str(i);
           for j in s:
               digits.append(j)
           if int(digits[0]) != 4:
              first=(int(digits[0])*'X')
           else:
              first='XL'
           if int(digits[1]) != 0:
              second=irmap[int(digits[1])]
           else:
              second=" "
           rn =(first+second)
           irmap[i]=rn

    for k in range(50,100):
        if k not in values:
            digits=[]
            s=str(k);
            for l in s:
                digits.append(l)
            if int(digits[0]) != 9:
                first = 'L'
                second=irmap[int(k-50)]
            else:
                first = 'XC'
                if int(digits[1]) != 0:
                   second=irmap[int(digits[1])]
                else:
                   second=" "
            rn =(first+second)
            irmap[k]=rn


    print(irmap)




                #: elif num > 50 and num < 100:
#         digits =[]
#         s=str(num)
#         for i in s:
#             digits.append(i)
#         if int(digits[0]) != 9:
#            first='L'
#        else:
#            first=


convertI2R(48)
