# this example was generate for chatgpt

# # instance from native
# from queue import Queue
# queue = Queue()

# # Enqueue Operation
# queue.put(10)
# queue.put(20)
# queue.put(30)

# # dequee Operation
# item = queue.get()
# print(item)

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None
        
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return None

queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.size())

item = queue.dequeue()
print(item) # 10

print(queue.peek()) # 20
