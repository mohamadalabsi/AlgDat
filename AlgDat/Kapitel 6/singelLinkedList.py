class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    def insert_at_beginning (self, data):
        new_node = Node(data)
        new_node.next=self.head
        self.head=new_node
    def insert_at_position(self , pos, data):
        new_node = Node(data)
        temp=self.head
        for i in range (pos-1):
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node    


    def delete_at_beginning (self):
        temp=self.head   
        self.head = temp.next
        temp.next=None
    def delete_at_end(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None     
            

    def delete_node(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example usage
ll = LinkedList()
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
ll.insert_at_beginning(55)
ll.insert_at_position(2,33)
ll.print_list()
ll.delete_at_beginning()
ll.delete_node(33)
ll.delete_at_end()
ll.print_list()
