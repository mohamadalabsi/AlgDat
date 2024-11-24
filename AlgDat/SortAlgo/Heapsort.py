def heapify(arr, n, i):
    """
    Maintain the max-heap property for a subtree rooted at index i.
    :param arr: Array representation of the heap
    :param n: Size of the heap
    :param i: Root index of the subtree
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Recursively heapify the affected subtree

def heap_sort(arr):
    """
    Perform Heap Sort using Max-Heapify.
    :param arr: Input array to be sorted
    """
    n = len(arr)

    # Step 1: Build a Max Heap
    for i in range(n // 2 - 1, -1, -1):  # Start from the last non-leaf node
        heapify(arr, n, i)

    # Step 2: Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap the root with the last element
        heapify(arr, i, 0)  # Heapify the reduced heap

# Example Usage
arr = [65, 0, 36, 44, 6]
heap_sort(arr)
print("Sorted array is:", arr)
