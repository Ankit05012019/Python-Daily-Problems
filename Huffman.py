import re
import subprocess

mydir={"a":3,"b":5,"c":6}

def huffman_code(mydict):
    mylist=[]
    for letter in mydir:
        mylist.append(mydir[letter])
    while len(mylist)>0:    
        maxfreq=max(mylist)

huffman_code(mydir)
   
