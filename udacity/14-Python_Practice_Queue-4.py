# this example was generate for chatgpt

class Queue:

    def __init__(self, max_size=None):
        self.queue      = []
        self.max_size   = max_size

    def enqueue(self, item):
        if self.max_size is None or len(self.queue) < self.max_size:
            self.queue.append(item)
        else:
            print("Queue is full. Unable to enqueue item:", item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def is_full(self):
        return self.max_size is not None and len(self.queue) == self.max_size
    
    def size(self):
        return len(self.queue)
    
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return None
    def clear(self):
        self.queue = []

# validate the queue
queue = Queue(max_size=3)
queue.enqueue(10)
queue.enqueue(20)
# validate if is full
print(queue.is_full())
queue.enqueue(30)
# validate if is full
print(queue.is_full())
# insert another 
queue.enqueue(40)

item = queue.dequeue()
print(item)  # Output: 10

print(queue.size())  # Output: 2

queue.clear()

print(queue.is_empty())  # Output: True