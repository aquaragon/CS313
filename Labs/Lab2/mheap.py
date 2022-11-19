class max_heap(object):
    """Binary max-heap

    Supports most standard heap operations (insert, peek, extract_max).
    Can be used for building a priority queue or heapsort. Since Python
    doesn't have built-in arrays, the underlying implementation uses a
    Python list instead. When initialized, max_heap creates a new list of
    fixed size or uses an existing list.
    """

    """
        Attributes:
            size:
            data:
            
            
        Methods:
            get_heap(): returns the heap
            insert(): inserts a passed in value into the heap, swaps to retain heap if necessary   
            peek():returns the max value of the heap
            extract_max(): returns and removes the max value from the heap
            __heapify():ensures the list is still a heap by going through the locations and comparing their left and right children to current nodes self
            build_heap(): creates a heap from a given list
            get_parent():determines parent location of passed in location
            get_left():determines left child location from passed in location
            get_right():determines right child location from passed in location
            __swap():swaps the values of the two passed in locations
    """



    def __init__(self, size = 20, data = None):
        """Initialize a binary max-heap.

        size: Total capacity of the heap.
        data: List containing the desired heap contents. 
              The list is used in-place, not copied, so its contents 
              will be modified by heap operations.
              If data is specified, then the size field is ignored."""

        # Add to this constructor as needed
        if data is not None:
            self.max_size = len(data)
            self.length = len(data)
            self.heap = data
        else:
            self.max_size = size
            self.length = 0
            self.heap = [None] * size
        
    def get_heap(self):
        return self.heap


    def insert(self, data):
        """Insert an element into the heap.

        Raises IndexError if the heap is full."""
        # Tips : insert 'data' at the end of the list initially
        #      : swap with its parent until the parent is larger or you 
        #      : reach the root

        if self.length == self.max_size:
            raise IndexError
        else:
            self.length += 1
            current = self.length - 1
            self.heap[current] = data
            while current != 0 and self.heap[self.__get_parent(current)] < self.heap[current]:
                self.__swap(self.__get_parent(current), current)
                current = self.__get_parent(current)






    def peek(self):
        """Return the maximum value in the heap."""
        return self.heap[0]

    def extract_max(self):
        """Remove and return the maximum value in the heap.

        Raises KeyError if the heap is empty."""
        # Tips: Maximum element is first element of the list
        #     : swap first element with the last element of the list.
        #     : Remove that last element from the list and return it.
        #     : call __heapify to fix the heap
        if self.length == 0:
            raise KeyError
        else:
            self.__swap(0, self.length - 1)
            max = self.heap[self.length - 1]
            self.heap[self.length -1] = None
            self.length -= 1
            self.__heapify(0, self.length - 1)
        return max


    def __heapify(self, curr_index, list_length = None):
        # helper function for moving elements down in the heap
        # Page 157 of CLRS book
        # I did indeed use the code from the text book
        left = self.__get_left(curr_index)
        right = self.__get_right(curr_index)
        if left <= self.length-1 and self.heap[left] > self.heap[curr_index]:
            largest_loc = left
        else:
            largest_loc = curr_index
        if right <= self.length - 1 and self.heap[right] > self.heap[largest_loc]:
            largest_loc = right
        if largest_loc != curr_index:
            self.__swap(curr_index, largest_loc)
            self.__heapify(largest_loc, self.length)


    def build_heap(self):
        # builds max heap from the list l.
        # Tip: call __heapify() to build to the list
        #    : Page 157 of CLRS book
        start = (self.length -1  // 2) - 1
        for j in range(start, -1, -1):
            self.__heapify(j, self.length -1)


    ''' Optional helper methods may be used if required '''
    ''' You may create your own helper methods as required.'''
    ''' But do not modify the function definitions of any of the above methods'''

    def __get_parent(self, loc):
        # left child has odd location index
        # right child has even location index
        # if loc % 2 == 0:
        #     parent = int((loc - 2) / 2)
        # else:
        parent = int((loc - 1) / 2)
        return parent

    def __get_left(self, loc):
        return 2*loc + 1

    def __get_right(self, loc):
        return 2*loc + 2
        

    def __swap(self, a, b):
        # swap elements located at indexes a and b of the heap
        temp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = temp
    



    

def heap_sort(l):
    """Sort a list in place using heapsort."""
    # Note: the heap sort function is outside the class
    #     : The sorted list should be in ascending order
    # Tips: Initialize a heap using the provided list
    #     : Use build_heap() to turn the list into a valid heap
    #     : Repeatedly extract the maximum and place it at the end of the list
    #     : Refer page 161 in the CLRS textbook for the exact procedure
    mh = max_heap(len(l), l)
    sorted_list = [None] * len(l)
    mh.build_heap()
    for i in range(0, mh.length):
        sorted_list[(len(sorted_list) - i - 1)] = mh.extract_max()

    return sorted_list