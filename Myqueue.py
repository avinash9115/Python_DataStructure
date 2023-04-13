class Queue:
   def __init__(self):
      self.queue = list()

   def addtoq(self,data):
# Insert method to add element
        if data not in self.queue:
            self.queue.insert(0,data)
            return True
        return False

   def size(self):
      return len(self.queue)
   
   def removefromq(self):
      if len(self.queue)>0:
         return self.queue.pop()
      return ("No elements in Queue!")


TheQueue = Queue()
TheQueue.addtoq("Mon")
TheQueue.addtoq("Tue")
TheQueue.addtoq("Wed")
print(TheQueue.size())
print(TheQueue.removefromq())