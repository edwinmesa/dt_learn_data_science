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
    
    
