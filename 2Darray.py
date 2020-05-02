"""Implement a 2D iterator class. It will be initialized with an array of arrays, and should implement the following methods:

next(): returns the next element in the array of arrays. If there are no more elements, raise an exception.
has_next(): returns whether or not the iterator still has elements left.


class iterator2D():

    def __init__(self,arry):
        # Should we implement it with rows and columns
        # as it is a 2D array ?!
        # aye
         self.count=0
         self.arry=arry
         # Wdyt ?! looks good sire . if you can just leave commects i will try and implement the code.
         # Done.

         # This way you can keep track of rows and column
         # currently the iterator is at !
         self.current_row = 0
         self.current_col = 0
         self.maxrow = len(arry)
         self.maxcol = len(arry[0]) # if we will pass  arrays of different length within the array this would not hold true
         # right ? like [[1.2],[1,2,3],[5]]

    def next(self):
        try:
            # TODO: We can update the fetch logic with correct
            # params.
           if self.arry[self.count]:
              return self.arry[self.count]
        except ValueError:
              return "There are no more elements in the array"
        finally:
            # Update the values of rows and columns,
            # switching to next row when boundary of row 1 been
            # reached.
             self.count += 1

    def has_next(self):
        try:
            # Check if the boundary has been reached, if yes
            # move to the next row, else if global boundary reached
            # error out or raise exception.

          if self.arry[self.count]:
             print("array has a element at the next index")
        except:
            print("no more elements in the array")

obj=iterator2D([[1,2],[2,3],[3,4]])
nextelement=obj.next()
print(nextelement)
obj.has_next()
nextelement2=obj.next()
print(nextelement2)
obj.has_next()
nextelement3=obj.next()

print (nextelement3)
obj.has_next()"""


# The above problem with parsing of individaul element in the 2D array

class iterator2D2:

    def __init__(self,arry):

        self.count = 0
        self.current_row = 0
        self.current_col = 0
        self.arry=arry

    def next(self):

           try:
                if self.current_row < len(self.arry) and self.current_col < len(self.arry[self.current_row]) :
                   print (self.arry[self.current_row][self.current_col])

                #if self.current_col <= (len(self.arry[self.current_row]) -1):
                self.current_col += 1

                if self.current_col >= len(self.arry[self.current_row]): # and self.current_row != (len(self.arry) -1 ):
                          self.current_row += 1
                          self.current_col = 0

           except IndexError:

                 print("IndexError:no more elements in the array")

    def has_next(self):

          length=len(self.arry)
          if self.current_row >= length:
              print("no next elements")
          elif self.current_row == (length -1) and self.current_col > (len(self.arry[self.current_row]) -1):
              print ("no next element to iterate")
          else:
              print("there is a next element in array")



obj=iterator2D2([[1,2],[],[2,3,7]])
obj.next()

obj.next()
obj.has_next()
obj.next()
obj.has_next()

obj.next()

obj.next()
obj.has_next()
obj.next()
obj.next()
obj.has_next()
