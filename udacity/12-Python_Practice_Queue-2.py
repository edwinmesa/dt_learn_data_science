# this example was generate for chatgpt
# when we use an a list
# queue = []

# # Enqueue operation
# queue.append(10)
# queue.append(20)
# queue.append(30)
# # Dequeue Operation
# item = queue.pop(0)
# print(item) # Output: 10


class Queue:
    def __init__(self) -> None:
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


queue = Queue()
# enqueue operation
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
# Dequee Operation
item = queue.dequeue()
print(item)