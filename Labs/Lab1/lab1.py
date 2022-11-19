class Node(object):
    """
    A class to represent a node.

    ...

    Attributes
    ----------
    data : int or float
        An individual character or number to be stored in a node
    next_node : object of class Node
        A pointer to the next node in a stack or queue

    Methods
    -------
    setData(data):
        Updates the value of data attribute of Node
    setNext(next_node):
        Updates the value of next_node attribute of Node
    getData():
        Returns the value of data attribute
    getNext():
        Returns the value of next_node attribute
    """
    def __init__(self, data = None, next_node = None):
        """
        Constructs (or initializes) the attributes for an object of the class

        ...

        Parameters
        ----------
        data : int or float
            An individual character or number to be stored in a node
        next_node : object of class Node
            A pointer to the next node in a stack or queue

        """
        self.__data = data
        self.__next_node = next_node

    def setData(self, data):
        '''Set the "data" data field to the corresponding input.'''
        self.__data = data

    def setNext(self, next_node):
        '''Set the "next_node" data field to the corresponding input.'''
        self.__next_node = next_node

    def getData(self):
        '''Return the "data" data field.'''
        return self.__data

    def getNext(self):
        '''Return the "next_node" data field.'''
        return self.__next_node

class Queue(object):
    """Provide class dosctring"""
    def __init__(self):
        self.__head = None
        self.__tail = None

    def __str__(self):
        '''Loop through your queue and print each Node's data.'''
        q_string = '['
        iterator = self.__head
        while iterator != None:
            if iterator.getNext() == None:
                q_string += str(iterator.getData()) #grabs current Node's data and adds it to string
            else:
                q_string += str(iterator.getData()) + ', '
            iterator = iterator.getNext()
        q_string += ']'
        return q_string




    def enqueue(self, newData):
        '''Create a new node whose data is newData and whose next node is null
        Update head and tail.'''
        # Hint: Think about what's different for the first node added to the Queue
        newNode = Node(newData)
        if self.__head == None:
            self.__head = newNode
            self.__tail = newNode
        else:
            self.__tail.setNext(newNode)
            self.__tail = newNode


    def dequeue(self):
        '''Return the head of the Queue
        Update head.'''
        #  Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #          to hold important information
        #  Hint: Return null on a empty Queue
        # Hint: Return the element(data) that is dequeued.
        if self.__head == None:
            raise IndexError
        else:
            data = self.__head.getData()
            self.__head = self.__head.getNext()
        return data




    def isEmpty(self):
        '''Check if the Queue is empty.'''
        return self.__head == None




class Stack(object):
    """Provide class dosctring"""
    def __init__(self):
        ''' We want to initialize our Stack to be empty.'''
        self.__top = None

    def __str__(self):
        '''Loop through your stack and print each Node's data.'''
        s_string = '['
        iterator = self.__top
        while iterator != None:
            if iterator.getNext() == None:
                s_string += str(iterator.getData())
            else:
                s_string += str(iterator.getData()) + ', '
            iterator = iterator.getNext()
        s_string += ']'
        return s_string

    def push(self, newData):
        '''We want to create a node whose data is newData and next node is top.
        Push this new node onto the stack
        Update top'''
        if self.__top == None:
            newTop = Node(newData)
            self.__top = newTop
        else:
            newTop = Node(newData,self.__top)
            self.__top = newTop


    def pop(self):
        ''' Return the Node that currently represents the top of the stack.
        Update top'''
        # Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #         to hold important information
        # Hint: Return null on a empty stack
        # Hint: Return the element(data) that is popped
        topData = None
        if self.__top != None:
            topData = self.__top.getData()
            self.__top =  self.__top.getNext()
        return topData


    def isEmpty(self):
        '''Check if the Stack is empty.'''
        return self.__top == None


def isPalindrome(s):
    '''Use your Queue and Stack class to test wheather an input is a palindrome.'''
    myStack = Stack()
    myQueue = Queue()


    s_string = ''
    s_count = 0
    for i in s:
        if i != ' ':
            myStack.push(i)
            s_count += 1
    for a in range (s_count):
        s_string += myStack.pop()
    s_string = s_string.lower()
    print("stack data = ", s_string)


    q_string = ''
    q_count = 0
    for j in s:
        if j != ' ':
            myQueue.enqueue(j)
            q_count += 1
    for b in range (q_count):
        q_string += myQueue.dequeue()
    q_string = q_string.lower()
    print("queue data = ", q_string)

    return q_string == s_string


class TwoStackQueue(object):
    '''Implements a queue from a 2 stacks by pushing on to the first stack when enqueueing then pops onto the second stack and pops again for the dequeue'''
    def __init__(self):
        self.__stack1 = Stack()
        self.__stack2 = Stack()

    def __str__(self):
        ''' outputs the entire queue into a string while re-implementing the the queue because we can only enqueue and dequeue and dont have access to a pointer so that we can temporarily iterate with'''
        tsq_string = "["
        if(self.__stack2.isEmpty()):
            while not self.__stack1.isEmpty():
                self.__stack2.push(self.__stack1.pop())
        while not self.__stack2.isEmpty():
            data = self.__stack2.pop()
            self.__stack1.push(data)
            tsq_string += str(data) + ', '
        tsq_string = tsq_string[:-2]
        tsq_string += ']'
        return tsq_string

    def enqueue(self, newData):
        self.__stack1.push(newData)

    def dequeue(self):
        if (self.__stack1.isEmpty() and self.__stack2.isEmpty()):
            return None
        while not self.__stack1.isEmpty():
            self.__stack2.push(self.__stack1.pop())
        return self.__stack2.pop()

    def isEmpty(self):
        return self.__stack1.isEmpty()

def isPalindromeEC(s):
    '''Implement if you wish to do the extra credit.'''

    myStack = Stack()
    myQueue = TwoStackQueue()


    s_string = ''
    s_count = 0
    for i in s:
        if i != ' ':
            myStack.push(i)
            s_count += 1
    for a in range (s_count):
        s_string += myStack.pop()
    s_string = s_string.lower()
    print("stack data = ", s_string)


    q_string = ''
    q_count = 0
    for j in s:
        if j != ' ':
            myQueue.enqueue(j)
            q_count += 1
    for b in range (q_count):
        q_string += myQueue.dequeue()
    q_string = q_string.lower()
    print("queue data = ", q_string)

    return q_string == s_string
