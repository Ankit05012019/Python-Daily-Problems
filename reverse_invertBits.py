#Given a 32 bit integer reverse its bits

def reverseBits(n) :

    rev = 0

    # traversing bits of 'n' from the right
    while (n > 0) :

        # bitwise left shift 'rev' by 1
        rev = rev << 1

        # if current bit is '1'
        if (n & 1 == 1) :
            rev = rev ^ 1

        # bitwise right shift 'n' by 1
        n = n >> 1


    # required number
    return rev

#n = 11
#print(bin(11))
#print(bin(reverseBits(n)))

def reverseBits(num,bitSize):

    binary = bin(num)
    print(binary)


    reverse = binary[-1:1:-1]
    reverse = reverse + (bitSize - len(reverse))*'0'
    print(reverse)


reverseBits(23876,32)


def flipBits(n):

    #print (binary)
    flip_n=n ^ 1
    print(bin(n))
    print(bin(flip_n))


#print(bin(8))

#print(bin(8^(1 << 2)))



import math

def invertBits(num):

    x = int(math.log2(num)) + 1

    print (bin(num))

    for i in range(x):
        #print (i)
        num = (num ^ (1 << i))
        #print (bin(num))
    print(bin(num))

invertBits(8)


