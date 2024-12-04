class Node:
    WHITE = 0
    GRAY = 1
    BLACK = 2

    def __init__(self, node_id):
        self.id = node_id  # Node ID
        self.d = 0  # Distance (unused in this code)
        self.td = 0  # Time discovered
        self.tf = 0  # Time finished
        self.color = Node.WHITE  # Initial color
        self.pi = None  # Previous node (predecessor)
        self.edges = []  # Adjacency list (edges)

    def __repr__(self):
        return f"Node({self.id})"


class Edge:
    def __init__(self, node_to):
        self.to = node_to  # Node the edge points to


def add_node(node_id):
    """
    Create and return a new Node.
    """
    node = Node(node_id)
    print(f"Added node {node.id}")
    return node


def add_edge(node_from, node_to):
    """
    Add an edge from one node to another.
    """
    edge = Edge(node_to)
    node_from.edges.append(edge)
    print(f"Added edge from {node_from.id} to {node_to.id}")


def dfs_visit(node, time):
    """
    Perform a DFS visit on a node.
    """
    time[0] += 1
    node.td = time[0]
    node.color = Node.GRAY
    print(f"Node {node.id}, visited at t: {node.td}")

    for edge in node.edges:
        to_node = edge.to
        if to_node.color == Node.WHITE:
            to_node.pi = node
            dfs_visit(to_node, time)

    node.color = Node.BLACK
    time[0] += 1
    node.tf = time[0]
    predecessor_id = node.pi.id if node.pi else 0
    print(f"Node {node.id}, discovered at t: {node.td}, "
          f"finished at t: {node.tf}, predecessor: {predecessor_id}")


def dfs(nodes):
    """
    Perform DFS on a list of nodes.
    """
    time = [0]  # Single element list to hold time as a mutable reference
    for node in nodes:
        if node.color == Node.WHITE:
            dfs_visit(node, time)


if __name__ == "__main__":
    print("Hello DFS!")

    # Creating nodes
    np1 = add_node(1)
    np2 = add_node(2)
    np3 = add_node(3)
    np4 = add_node(4)
    np5 = add_node(5)
    np6 = add_node(6)

    # Adding edges
    add_edge(np1, np2)
    add_edge(np1, np3)
    add_edge(np2, np3)
    add_edge(np3, np4)
    add_edge(np4, np2)
    add_edge(np5, np4)
    add_edge(np5, np6)

    # Running DFS
    nodes = [np1, np2, np3, np4, np5, np6]
    dfs(nodes)
