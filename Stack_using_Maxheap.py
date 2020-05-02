"""Implement a stack API using only a heap. A stack implements the following methods:

push(item), which adds an element to the stack
pop(), which removes and returns the most recently added element (or throws an error if there is nothing on the stack)
Recall that a heap has the following operations:

push(item), which adds a new key to the heap
pop(), which removes and returns the max value of the heap"""

class myHeap:


    def __init__(self):
       self.heap=[0]
       #self.pos=pos
       #self.root=(len(self.heap[]) + 1)
      # self.right=0
       #self.left=0
       self.recent=0

    def parent(self,pos):
        return pos//2

    def left(self,pos):
        return  pos * 2

    def right(self,pos):
        return (pos * 2) + 1

    def swap(self,left,right):

       self.heap[left],self.heap[right]  = self.heap[right],self.heap[left]
       return self.heap[left],self.heap[right]

    def isLeaf(self, pos):
        if pos >= ((len(self.heap)-1)//2) and pos <= (len(self.heap) -1):
            return True
        return False

    def heapify(self,pos):

        #self.left(pos)
        #self.right(pos)
       if not self.isLeaf(pos):
           if self.heap[pos] < self.heap[self.left(pos)] or self.heap[pos] < self.heap[self.right(pos)]:

                 if self.heap[self.left(pos)] > self.heap[self.right(pos)]:
                    self.swap(pos ,self.left(pos))
                    self.heapify(self.left(pos))

                 else:
                     self.swap(pos,self.right(pos))
                     self.heapify(self.right(pos))

    def push(self,num):

       self.heap.append(num)
       #self.heapify((len(self.heap) - 1))
       current = (len(self.heap) - 1)

       print(self.heap[current])
       while self.heap[current] > self.heap[self.parent(current)] and current > 1:
             #print(f"new parent {self.heap[self.parent(current)]}")
             self.swap(current,self.parent(current))
             current = self.parent(current)
       print (current)
       self.recent=current
       return self.heap




    def pop(self):

        if len(self.heap) <= 1:
            print("no elements to pop")

        else:
             print(f"last added element is at {self.recent}")
             self.swap(len(self.heap)-1,self.recent)
             self.heap.pop()
             print (self.heap)
             #print (self.recent)
             self.heapify(self.recent)
        return self.heap



mynewheap=myHeap()
heap=mynewheap.push(5)
heap=mynewheap.push(10)
heap=mynewheap.push(15)
heap=mynewheap.push(55)
heap=mynewheap.push(18)
heap=mynewheap.push(28)

print(heap)

heap2=mynewheap.pop()
