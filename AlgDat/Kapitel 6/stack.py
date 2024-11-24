# from pprint import  pprint as pp

# stack=[]
# stack.append(1)
# stack.append(2)
# stack.append(3)
# stack.append(("mohammad",23))
# stack.append(4)

# stack.pop()
# pp(stack[3][1])
# pp(stack)

# here like u see u can use pre build collection like list  ,   java with linked list ,  stack and deque see the images 

# in stacks we can use linked list or normal array
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None  # Pointer to the top of the stack

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            print("Stack underflow")
            return None
        popped_value = self.top.value
        self.top = self.top.next
        return popped_value

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.top.value

    def is_empty(self):
        return self.top is None



stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.peek())  # Output: 30
print(stack.pop())   # Output: 30
print(stack.pop())   # Output: 20
print(stack.is_empty())  # Output: False
