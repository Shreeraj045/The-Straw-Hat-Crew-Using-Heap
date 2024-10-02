class Heap:
    def __init__(self, comparison_function, init_array):
        self.init_array = init_array
        self.comparator = comparison_function
        # Write your code here
        if self.init_array:
            for i in range((len(self.init_array) - 2) // 2, -1, -1):
                self._downheap(i)
        pass

    def insert(self, value):
        self.init_array.append(value)
        self._upheap(len(self.init_array)-1)
        return

    def extract(self):
        if len(self) == 0:
            return None
        self._swap(0, len(self) - 1)
        element = self.init_array.pop()
        self._downheap(0)
        return element

    def top(self):
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
        self.   init_array[index1], self.init_array[index2] = self.init_array[index2], self.init_array[index1]

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
    def copy_heap(self):
        return self.init_array[:]

heap = Heap(lambda x, y: x < y, [1,5,15,23,22,16,17])
print(heap.init_array)