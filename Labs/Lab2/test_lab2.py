import unittest
import pqueue
import mheap


class T0_pqueue_insert(unittest.TestCase):


    def test_1_pq_insert(self):
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        pq.insert(4)
        pq.insert(5)
        pq_list = [element for element in pq]
        self.assertEqual(pq_list, [5,4,2,1,3])
        print("\n")

    def test_2_pq_insert(self):
        '''2nd addtinal required unittest, Check that an indexerror is raised when inserting to a heap that is already full'''
        print("Testing insert on a full heap, should raise Index Error")
        print("\n")
        mh = mheap.max_heap(3)
        mh.insert(1)
        mh.insert(7)
        mh.insert(9)
        with self.assertRaises(IndexError):
            mh.insert(4)
        print("\n")

    def test_3_pq_insert(self):
        '''Self-added unitestt 1 of the 6 extra, testing random number inserts'''
        pq = pqueue.pqueue(9)
        pq.insert(7)
        pq.insert(67)
        pq.insert(10)
        pq.insert(37)
        pq.insert(4)
        pq.insert(3)
        pq.insert(24)
        pq.insert(57)
        pq.insert(87)
        self.assertEqual(pq.get_pqueue(), [87, 67, 24, 57, 4, 3, 10, 7, 37])

    def test_4_pq_insert(self):
        '''Seld-added unitest 3 of the 6 extra, testing list doesnt expand on each insert and should print None for empty locations'''
        print("\n")
        pq = pqueue.pqueue(7)
        pq.insert(67)
        pq.insert(10)
        self.assertEqual(pq.get_pqueue(), [67, 10, None, None, None, None, None])

    def test_4_pq_insert(self):
        '''Self-added unitestt 6 of the 6 extra, testing insert and extracting the same number on multiple numbers'''
        print("\n")
        mh = mheap.max_heap(4)
        mh.insert(2)
        mh.insert(6)
        mh.insert(8)
        mh.insert(9)

        mh.extract_max()
        mh.insert(10)

        mh.extract_max()
        mh.insert(11)

        self.assertEqual(mh.get_heap(), [11, 8, 6, 2])



class T1_pqueue_peek(unittest.TestCase):

    def test_1_pq_peek(self):
        print("Just return the fist element of the queue.")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        self.assertEqual(pq.peek(), 3)
        print("\n")

    def test_2_pq_peek(self):
        '''Self-added unitestt 2 of the 6 extra, checks peek on an empty heap should return None'''
        print("\n")
        pq = pqueue.pqueue(4)
        self.assertEqual(pq.peek(), None)

class T2_pqueue_extract_max(unittest.TestCase):

    def test_1_pq_extract_max(self):
        print("extract and return the maximum element of the queue")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        self.assertEqual(pq.extract_max(), 3)
        print("\n")

    def test_2_pq_extract_max(self):
        '''3rd additional required unittest, testing extract max on an empty heap'''
        print("Testing extract max on a empty list")
        print("\n")
        pq = pqueue.pqueue(7)
        with self.assertRaises(KeyError):
            pq.extract_max()
        print("\n")

    def test_3_pq_extra_max(self):
        '''4th additional required unittest, Check if an object of pqueue is still a valid heap after the following series of insert() and extract_max() calls on the same pqueue object'''
        print("\n")
        pq = pqueue.pqueue(4)
        pq.insert(4)
        pq.insert(3)
        pq.insert(2)
        pq.insert(1)
        pq.extract_max()
        pq.extract_max()
        self.assertEqual(pq.get_pqueue(), [2, 1, None, None])


class T4_test_build_heap(unittest.TestCase):

    def test_build_heap_1(self):
        '''Extra Required unittest #1 check that build_heap() properly builds a max heap'''
        print("\n")
        list_to_test = [18,20,30,17,50]
        mh = mheap.max_heap(len(list_to_test), list_to_test)
        mh.build_heap()
        self.assertEqual(mh.get_heap(), [50,20,30,17,18])

    def test_build_heap_2(self):
        '''Self-added unitestt 5 of the 6 extra, testing buildheap on a already heaped list'''
        print("\n")
        list_to_test = [50,20,30,17,18]
        mh = mheap.max_heap(len(list_to_test), list_to_test)
        mh.build_heap()
        self.assertEqual(mh.get_heap(), [50,20,30,17,18])



class T5_heap_sort(unittest.TestCase):

    def test_heap_sort_1(self):
        print("\n")
        to_sort_list = [10,24,3,57,4,67,37,87,7]
        sorted_list = mheap.heap_sort(to_sort_list)

        self.assertEqual(sorted_list, [3, 4, 7, 10, 24, 37, 57, 67, 87])
        print("\n")

    def test_heap_sort_2(self):
        '''Self-added unitestt 4 of the 6 extra, test heap sort on a already sorted list'''
        to_sort_list = [1,2,3,4,5]
        sorted_list = mheap.heap_sort(to_sort_list)
    
        self.assertEqual(sorted_list, [1, 2, 3, 4, 5])
    
    
if __name__ == '__main__':
    unittest.main()