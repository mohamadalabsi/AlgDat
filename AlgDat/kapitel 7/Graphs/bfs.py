# Node class to represent a graph node
class Node:
    def __init__(self, id):
        self.id = id            # Unique identifier for the node
        self.color = "WHITE"    # Initial color (unvisited)
        self.d = float('inf')   # Distance from the start node (initially infinite)
        self.pi = None          # Predecessor node (parent in BFS tree)
        self.edges = []         # List to store adjacent edges (neighbors)

# Queue class implemented from scratch
class Queue:
    def __init__(self):
        self.items = []  # Use a Python list to simulate a queue

    def enqueue(self, item):
        self.items.append(item)  # Add an item to the end of the queue

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)  # Remove and return the item at the front
        return None  # Return None if the queue is empty

    def is_empty(self):
        return len(self.items) == 0  # Check if the queue is empty

# BFS function
def bfs(start_node):
    # Initialize the start node
    start_node.color = "GRAY"   # Mark it as discovered
    start_node.d = 0            # Distance from itself is 0
    start_node.pi = None        # No predecessor
    queue = Queue()             # Create a new queue
    queue.enqueue(start_node)   # Enqueue the start node

    # BFS loop
    while not queue.is_empty():
        u = queue.dequeue()     # Dequeue the front node
        print(f"Processing Node {u.id}, Distance: {u.d}, Predecessor: {u.pi.id if u.pi else 'None'}")
        
        for neighbor in u.edges:  # Iterate over neighbors of the current node
            if neighbor.color == "WHITE":  # If the neighbor is unvisited
                neighbor.color = "GRAY"    # Mark it as discovered
                neighbor.d = u.d + 1       # Update the distance
                neighbor.pi = u            # Set the current node as its predecessor
                queue.enqueue(neighbor)    # Enqueue the neighbor
        
        u.color = "BLACK"  # Mark the node as fully processed

# Example usage
if __name__ == "__main__":
    # Create nodes
    nodes = [Node(i) for i in range(1, 7)]

    # Create edges (graph structure)
    nodes[0].edges.extend([nodes[1], nodes[2]])  # Node 1 → Node 2, Node 3
    nodes[1].edges.append(nodes[3])             # Node 2 → Node 4
    nodes[2].edges.append(nodes[3])             # Node 3 → Node 4
    nodes[3].edges.extend([nodes[4], nodes[5]]) # Node 4 → Node 5, Node 6

    # Perform BFS starting from Node 1
    bfs(nodes[0])
