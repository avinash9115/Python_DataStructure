class Stack:
  def __init__(mystack):
      mystack.stack = []

  def add(mystack, data):
# Use list append method to add element
      if data not in mystack.stack:
         mystack.stack.append(data)
         return True
      else:
         return False
# Use peek to look at the top of the stack
  def peek(mystack):     
	   return mystack.stack[-1]

mystack = Stack()
mystack.add("Mon")
mystack.add("Tue")
mystack.peek()
print(mystack.peek())
mystack.add("Wed")
mystack.add("Thu")
print(mystack.peek())
mystack.add("guruwar")
mystack.add("ravivar")
print(mystack.peek())