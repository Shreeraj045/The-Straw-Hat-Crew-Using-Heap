from heap import Heap  # Assuming the Heap class is in a file called 'heap.py'

# Comparison functions for min-heap and max-heap
def min_comparator(x, y):
    return x < y  # Return True if x is smaller than y (min-heap)

def max_comparator(x, y):
    return x > y  # Return True if x is larger than y (max-heap)

def main():
    print("Testing Min-Heap:")
    min_heap = Heap(min_comparator,[])

    # Insert elements into the min-heap
    for value in [10, 4, 15, 20, 3, 6]:
        min_heap.insert(value)
        print(f"After inserting {value}:")
        min_heap.print_tree()  # Print the heap in tree format after each insertion

    # Extract elements from the min-heap
    print("\nExtracting elements from min-heap:")
    while len(min_heap) > 0:
        top_value = min_heap.extract()
        print(f"After extracting {top_value}:")
        min_heap.print_tree()  # Print the heap in tree format after each extraction

    print("\nTesting Max-Heap:")
    max_heap = Heap(max_comparator,[])

    # Insert elements into the max-heap
    for value in [10, 4, 15, 20, 3, 6]:
        max_heap.insert(value)
        print(f"After inserting {value}:")
        max_heap.print_tree()  # Print the heap in tree format after each insertion

    # Extract elements from the max-heap
    print("\nExtracting elements from max-heap:")
    while len(max_heap) > 0:
        top_value = max_heap.extract()
        print(f"After extracting {top_value}:")
        max_heap.print_tree()  # Print the heap in tree format after each extraction

if __name__ == "__main__":
    main()
