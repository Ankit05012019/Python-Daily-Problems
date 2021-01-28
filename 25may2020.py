# check if a integer is palindrome
def myfunc(int):

   mystr=str(int)
   newstr=mystr[::-1]
   print(mystr)
   print(newstr)

   if  newstr == mystr :
      print("yes plaindrome")
   else:
      print ("not palindrome")

myfunc(323)
