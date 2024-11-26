# now here priority queue uses heap 
# u can use priority queue with a simple  list and for the best like heap sort or use pre build collection like heapq , and in java PriorityQueue 
# from scratch u have to make it like a heap sort 





# Function to heapify a subtree rooted at index i
def max_heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Compare left child
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Compare right child
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest is not the root, swap and heapify the affected subtree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)


# Function to insert an element into the priority queue
def insert(arr, key):
    arr.append(key)
    i = len(arr) - 1
    parent = (i - 1) // 2

    # Bubble up to maintain max-heap property
    while i > 0 and arr[parent] < arr[i]:
        arr[i], arr[parent] = arr[parent], arr[i]
        i = parent
        parent = (i - 1) // 2


# Function to extract the maximum element from the priority queue
def extract_max(arr):
    if len(arr) == 0:
        raise IndexError("Priority queue is empty")
    if len(arr) == 1:
        return arr.pop()

    # Replace the root with the last element and heapify
    root = arr[0]
    arr[0] = arr.pop()  # Move the last element to the root
    max_heapify(arr, len(arr), 0)
    return root


# Function to peek at the maximum element without removing it
def peek(arr):
    if len(arr) == 0:
        raise IndexError("Priority queue is empty")
    return arr[0]


# Display the heap (optional, for debugging)
def display(arr):
    print(arr)


# Testing the Priority Queue
priority_queue = []

# Insert elements
insert(priority_queue, 10)
insert(priority_queue, 20)
insert(priority_queue, 15)
insert(priority_queue, 30)
insert(priority_queue, 25)

print("Heap after insertions:")
display(priority_queue)

# Peek at the max element
print("Max element:", peek(priority_queue))

# Extract max elements
print("Extracted:", extract_max(priority_queue))
print("Heap after extraction:")
display(priority_queue)

print("Extracted:", extract_max(priority_queue))
print("Heap after extraction:")
display(priority_queue)
