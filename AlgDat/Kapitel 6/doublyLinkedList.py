class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev=None
        

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
        new_node.prev=last
    def insert_at_beginning (self, data):
        new_node = Node(data)
        temp=self.head
        new_node.next=temp
        temp.prev=new_node
        self.head=new_node
        
        
    def insert_at_position(self , pos, data):
        new_node = Node(data)
        temp=self.head
        for i in range (pos-1):
            temp=temp.next
        new_node.prev=temp    
        new_node.next=temp.next
        temp.next.prev=new_node    
        temp.next=new_node
    
    def delete_at_beginning (self):
        temp=self.head   
        self.head=temp.next
        self.head.prev = None
        temp.next=None
    def delete_at_end(self):
        temp=self.head.next
        before=self.head
        while temp.next is not None:
            temp=temp.next
            before=before.next
        before.next=None     
        temp.prev=None
    
    def delete_at_position(self, pos ):
        temp=self.head.next
        before=self.head
        for i in range(pos-1):
            temp=temp.next
            before=before.next 
        before.next= temp.next
        temp.next.prev=before
        temp.next=None    
        temp.prev=None    

        
        
    def print_list(self):
        temp = self.head
        if self.head is None :
          print("the list is Empty ")
        else : 
          while temp:
              print(temp.data, end=" -> ")
              temp = temp.next
          print("None")    
        
        
        
        
ll=LinkedList() 
ll.insert_at_end(20)       
ll.insert_at_end(30)       
ll.insert_at_end(50)
ll.print_list()       
ll.insert_at_beginning(10)
ll.print_list()       
ll.insert_at_position(3,60)
ll.print_list()       
ll.delete_at_beginning()
ll.print_list()  
ll.delete_at_end()     
ll.print_list()       
ll.delete_at_position(1)
ll.print_list()       

