'''
Python Code to implement a heap with general comparison function
'''



class Heap:
    '''
    Class to implement a heap with general comparison function
    '''

    def __init__(self, comparison_function, init_array):
        '''
        Arguments:
            comparison_function : function : A function that takes in two arguments and returns a boolean value
            init_array : List[Any] : The initial array to be inserted into the heap
        Returns:
            None
        Description:
            Initializes a heap with a comparison function
            Details of Comparison Function:
                The comparison function should take in two arguments and return a boolean value
                If the comparison function returns True, it means that the first argument is to be considered smaller than the second argument
                If the comparison function returns False, it means that the first argument is to be considered greater than or equal to the second argument
        Time Complexity:
            O(n) where n is the number of elements in init_array
        '''
        self.init_array = init_array
        self.comparator = comparison_function
        # Write your code here
        if self.init_array:
            for i in range((len(self.init_array) - 2) // 2, -1, -1):
                self._downheap(i)
        pass

    def insert(self, value):
        '''
        Arguments:
            value : Any : The value to be inserted into the heap
        Returns:
            None
        Description:
            Inserts a value into the heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        self.init_array.append(value)
        self._upheap(len(self.init_array)-1)
        return

    def extract(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value extracted from the top of heap
        Description:
            Extracts the value from the top of heap, i.e. removes it from heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''

        if len(self) == 0:
            return None
        self._swap(0, len(self) - 1)
        element = self.init_array.pop()
        self._downheap(0)
        return element

    def top(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value at the top of heap
        Description:
            Returns the value at the top of heap
        Time Complexity:
            O(1)
        '''
        if len(self.init_array) == 0:
            return None
        return self.init_array[0]

    def __len__(self):
        return len(self.init_array)

    def _parent(self,index):
        return (index-1)//2

    def _left(self,index):
        return 2*index + 1

    def _right(self,index):
        return 2*index + 2

    def _has_left(self,index):
        return self._left(index) < len(self.init_array)

    def _has_right(self,index):
        return  self._right(index) < len(self.init_array)

    def _swap(self, index1, index2):
        self.init_array[index1], self.init_array[index2] = self.init_array[index2], self.init_array[index1]

    def _upheap(self, index):
        parent = self._parent(index)
        if index > 0 and self.comparator(self.init_array[index], self.init_array[parent]):
            self._swap(index, parent)
            self._upheap(parent)

    def _downheap(self, index):
        if self._has_left(index):
            left = self._left(index)
            small_child = left
            if self._has_right(index):
                right = self._right(index)
                if self.comparator(self.init_array[right], self.init_array[left]):
                    small_child = right
            if self.comparator(self.init_array[small_child], self.init_array[index]):
                self._swap(index, small_child)
                self._downheap(small_child)
                self._downheap(small_child)

    def print_tree(self):
        '''
        Prints the heap in a tree-like format.
        '''
        print(self.init_array)

# ######################      TESTING         #################

def min_comparator(x, y):
    return x < y
heap = Heap(min_comparator,[3,2,1,4,2,10,1])
heap.print_tree()
