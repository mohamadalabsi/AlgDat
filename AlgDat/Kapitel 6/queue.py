# from collections import deque
# myyList=deque()
# myyList.appendleft()

# here like u see u can use pre build collection like deque  ,   java with linked list 


# in queue we can use linked list or normal array
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None  # Points to the front of the queue
        self.rear = None   # Points to the rear of the queue

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = self.rear = new_node  # Both front and rear point to the new node
        else:
            self.rear.next = new_node         # Link the new node at the end of the queue
            self.rear = new_node              # Update the rear pointer

    def dequeue(self):
        if self.is_empty():
            print("Queue underflow")
            return None
        dequeued_value = self.front.value
        self.front = self.front.next          # Move front to the next node
        if self.front is None:               # If the queue becomes empty
            self.rear = None                 # Set rear to None as well
        return dequeued_value

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.front.value

    def is_empty(self):
        return self.front is None



queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.peek())  # Output: 10
print(queue.dequeue())  # Output: 10
print(queue.dequeue())  # Output: 20
print(queue.is_empty())  # Output: False
print(queue.dequeue())  # Output: 30
print(queue.is_empty())  # Output: True
