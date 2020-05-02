"""This problem was asked by Facebook.

Given an N by N matrix, rotate it by 90 degrees clockwise.

For example, given the following matrix:

[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
you should return:

[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
Follow-up: What if you couldn't use any extra space?

Upgrade to premium and get in-depth solutions to every problem, including this one.

If you liked this problem, feel free to forward it along so they can subscribe here! As always, shoot us an email if there's anything we can help with!

Master algorithms together on Binary Search. Create a room, invite your friends, and race to finish the problem!

No more? Snooze or unsubscribe."""

class Rotate:

   def __init__(self,arry):

       self.arry=arry
       self.current_row=0
       self.current_col=0
       self.rotated_arry=[]


   def print_arry(self):

       while self.current_row < len(self.arry):

             while self.current_col < len(self.arry[self.current_row]):
                  print(self.arry[self.current_row][self.current_col], end =" ")
                  self.current_col += 1

             print ("\n")
             self.current_row += 1
             self.current_col = 0
       print ("************end of array***************\n")

   def rotate_arry(self):
        print("rotating your array by 90 degree\n")
        last_row = len(self.arry) -1
        while self.current_col < len(self.arry):
              while last_row >= 0:
                  print (self.arry[last_row][self.current_col], end=" " )
                  last_row -=1
              print("\n")
              self.current_col +=1
              last_row=len(self.arry) -1



myarray=Rotate([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
myarray.print_arry()
myarray.rotate_arry()
