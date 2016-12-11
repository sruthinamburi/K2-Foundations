#program to perform insert from rear end and delete from front
queue =[]
#variable indicating the max size of the queue
maxSize = 4

#inserts an element from the rear end
def Enqueue(val):
   
   if len(queue) < maxSize:
    queue.append(val)
   else:
    print ("Overflow")
#deletes the element from the front end
def Dequeue():
   
   if len(queue) > 0:
    queue.pop(0)
   else:
    print ("Underflow")

#displays the current elements in the queue
def display():
 print ("queue currently contains:")
 for Item in queue:
  print (Item)

Enqueue(4)
Enqueue(6)
Enqueue(8)
display()
Dequeue()
display()
Dequeue()
display()
Enqueue(9)
display()
Dequeue()
Dequeue()
display()
Dequeue()







