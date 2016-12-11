#program to perform push, pop and dispaly operations in stack

stack =[]
#variable indicating the max size of the stack
maxSize = 3

#inserts an element on the top of the stack
def push(val):
   
   if len(stack) < maxSize:
    stack.append(val)
    
   else:
    print ("Overflow")
#deletes the topmost element on stack
def pop():
   
   if len(stack) > 0:
    stack.pop()
    
   else:
    print ("Underflow")

#displays the current elements in the stack
def display():
 print ("Stack currently contains:")
 for Item in stack:
  print (Item)

  
push(20)
push(40)
push(50)
display()

pop()
pop()

display()








