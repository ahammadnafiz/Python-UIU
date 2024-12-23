class Queue:
    def __init__(self, capacity = None):
        self._items = []
        self.capacity = capacity

    def enqueue(self, item):
        if self.is_full():
            raise QueueFullError('Queue has reached its capacity')

        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise QueueEmptyError("Can't dequeue from an empty queue")

        return self._items.pop(0)

    def front(self):
        if self.is_empty():
            raise QueueEmptyError("Queue is empty")

        return self._items[0]

    def rear(self):
        if self.is_empty():
            raise QueueEmptyError("Queue is empty")

        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def is_full(self):
        return self.capacity is not None and len(self._items) >= self.capacity

    def size(self):
        return len(self._items)

    def clear(self):
        self._items = []

    def contains(self, item):
        return item in self._items

    def to_list(self):
        return self._items.copy()
    
    def __str__(self):
        return f"Queue({self._items})"
    
    def __len__(self):
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)

class QueueEmptyError(Exception):
    pass

class QueueFullError(Exception):
    pass

# Example usage:
if __name__ == "__main__":
    # Create a queue with capacity of 3
    queue = Queue(capacity=3)
    
    # Test basic operations
    queue.enqueue("First")
    queue.enqueue("Second")
    queue.enqueue("Third")
    
    print(f"Queue: {queue}")  # Queue(['First', 'Second', 'Third'])
    print(f"Size: {queue.size()}")  # Size: 3
    print(f"Front item: {queue.front()}")  # Front item: First
    print(f"Rear item: {queue.rear()}")  # Rear item: Third
    
    # Test dequeue
    removed = queue.dequeue()
    print(f"Removed: {removed}")  # Removed: First
    print(f"New queue: {queue}")  # New queue: Queue(['Second', 'Third'])
    
    # Test iteration
    print("Items in queue:")
    for item in queue:
        print(item)
    
    # Test contains
    print(f"Contains 'Second': {queue.contains('Second')}")  # True
    
    # Test clear
    queue.clear()
    print(f"After clear: {queue}")  # After clear: Queue([])
    
    # Test error handling
    try:
        queue.dequeue()  # Should raise QueueEmptyError
    except QueueEmptyError as e:
        print(f"Error: {e}")
    
    # Test capacity limit
    queue = Queue(capacity=2)
    queue.enqueue(1)
    queue.enqueue(2)
    try:
        queue.enqueue(3)  # Should raise QueueFullError
    except QueueFullError as e:
        print(f"Error: {e}")
