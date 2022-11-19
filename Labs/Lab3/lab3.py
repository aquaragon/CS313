class Node(object):
    def __init__(self, data):
        self.parent = None
        self.left = None
        self.right = None
        self.data = data


class Tree(object):
    '''
    Creates a binary search tree of given integer data

    insert(self,data): inserts a new node into the tree with data passed in
    min(self): returns the smallest value of the BST
    max(self): returns the largest vale of the BST
    __find_node(self, data):Searches the BSY for a node holding the same value ass data passsed in, returns ptr to that node returns None if not found
    contains(self, data):Wrapper function to return true or false based on what find_node returns
    __traverse(self, curr_node, traversal_type): Does a traversal print of the function based on the passed in type, and the node passsed in
    find_successor(self, data): Looks for the successor node of the passed in node and returns the pointer to the successor, raise key error if node passed in is not in BST
    delete(self, data): Raises keyerror if desired node does not exist, deletes desired node that is passed in and has different maneuvers based on the amount of children the node has





    '''
    # Binary Search Tree
    # class constants
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

    def __init__(self):
        # Do not create any other private variables.
        # You may create more helper methods as needed.
        self.root = None

    def print(self):
        # Print the data of all nodes in order
        self.__print(self.root)


    def __print(self, curr_node):
        # Recursively print a subtree (in order), rooted at curr_node
        if curr_node is not None:
            self.__print(curr_node.left)
            print(str(curr_node.data), end=' ')  # save space
            self.__print(curr_node.right)
            

    def insert(self, data):
        # Find the right spot in the tree for the new node
        # Make sure to check if anything is in the tree
        # Hint: if a node n is None, calling n.data will cause an error
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
        else:
            ptr = self.root
            while ptr != None:
                if ptr.data > new_node.data:
                    if ptr.left == None:
                        new_node.parent = ptr
                        ptr.left = new_node
                        ptr = ptr.left
                    ptr = ptr.left
                else:
                    if ptr.right == None:
                        new_node.parent = ptr
                        ptr.right = new_node
                        ptr = ptr.right
                    ptr = ptr.right

    def min(self):
        # Returns the minimum value held in the tree
        # Returns None if the tree is empty
        if self.root == None:
            return None
        else:
            ptr = self.root
            while ptr.left != None:
                ptr = ptr.left
            return ptr.data

    def max(self):
        # Returns the maximum value held in the tree
        # Returns None if the tree is empty
        if self.root == None:
            return None
        else:
            ptr = self.root
            while ptr.right != None:
                ptr = ptr.right
            return ptr.data

    def __find_node(self, data):
        # returns the node with that particular data value else returns None
        ptr = self.root
        while ptr != None:
            if ptr.data == data:
                return ptr
            else:
                if ptr.data > data:
                    ptr = ptr.left
                else:
                    ptr = ptr.right
        return None

    def contains(self, data):
        # return True of node containing data is present in the tree.
        # otherwise, return False.
        # you may use a helper method __find_node() to find a particular node with the data value and return that node
        if self.__find_node(data) != None:
            return True
        else:
            return False

    def __iter__(self):
        # iterate over the nodes with inorder traversal using a for loop
        return self.inorder()

    def inorder(self):
        # inorder traversal : (LEFT, ROOT, RIGHT)
        return self.__traverse(self.root, Tree.INORDER)

    def preorder(self):
        # preorder traversal : (ROOT, LEFT, RIGHT)
        return self.__traverse(self.root, Tree.PREORDER)

    def postorder(self):
        # postorder traversal : (LEFT, RIGHT, ROOT)
        return self.__traverse(self.root, Tree.POSTORDER)

    def __traverse(self, curr_node, traversal_type):
        # helper method implemented using generators
        # all the traversals can be implemented using a single method
        
        #Yield data of the correct node/s
        if traversal_type == 1:
            if curr_node != None:
                yield curr_node.data
                yield from self.__traverse(curr_node.left, traversal_type)
                yield from self.__traverse(curr_node.right, traversal_type)
        elif traversal_type == 2:
            if curr_node != None:
                yield from self.__traverse(curr_node.left, traversal_type)
                yield curr_node.data
                yield from self.__traverse(curr_node.right, traversal_type)
        else:
            if curr_node != None:
                yield from self.__traverse(curr_node.left, traversal_type)
                yield from self.__traverse(curr_node.right, traversal_type)
                yield curr_node.data





    def find_successor(self, data):
        # Find the successor node
        # If the value specified by find_successor does NOT exist in the tree, then raise a KeyError
        # helper method to implement the delete method but may be called on its own
        # If the right subtree of the node is nonempty,then the successor is just 
        # the leftmost node in the right subtree.
        # If the right subtree of the node is empty, then go up the tree until a node that is
        # the left child of its parent is encountered. The parent of the found node will be the
        # successor to the initial node.
        # Note: Make sure to handle the case where the parent is None
    
    	# Return object of successor if found else return None
        if self.max() == data:
            return None
        elif self.root == None:
            raise KeyError
        ptr = self.__find_node(data)
        if ptr == None:
            raise KeyError
        else:
            if ptr.right == None:
                if ptr.parent.right == ptr:
                    while ptr.parent != None:
                        ptr = ptr.parent
                else:
                    ptr = ptr.parent
            else:
                ptr = ptr.right
                while ptr.left != None:
                    ptr = ptr.left
        return ptr

    def delete(self, data):
        # Find the node to delete.
        # If the value specified by delete does NOT exist in the tree, then don't change the tree and raise a KeyError
        # If you find the node and ...
        #  a) The node has no children, just set it's parent's pointer to None.
        #  b) The node has one child, make the nodes parent point to its child.
        #  c) The node has two children, replace it with its successor, and remove
        #       successor from its previous location.
        # Recall: The successor of a node is the left-most node in the node's right subtree.
        # Note: Make sure to handle the case where the parent is None
        ptr = self.__find_node(data)
        if ptr == None:
            raise KeyError
        elif self.root == None:
            raise KeyError
        else:
            if ptr.left == None and ptr.right == None:
                if ptr.parent.left == ptr:
                    ptr.parent.left = None
                else:
                    ptr.parent.right = None
            elif (ptr.left == None and ptr.right != None) or (ptr.left != None and ptr.right == None):
                if ptr.left != None:
                    if ptr.parent.right == ptr:
                        ptr.parent.right = ptr.left
                    else:
                        ptr.parent.left = ptr.left
                else:
                    if ptr.parent.right == ptr:
                        ptr.parent.right = ptr.right
                    else:
                        ptr.parent.left = ptr.right
            else:
                succ = self.find_successor(data)
                succ_data = succ.data
                self.delete(succ_data)
                ptr.data = succ_data





