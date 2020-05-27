"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        new_node = BSTNode(value)
        if self.value:
            if self.value > value:
                if self.left:
                    self.left.insert(value)
                else:
                    self.left = new_node
            else:
                if self.right:
                    self.right.insert(value)
                else:
                    self.right = new_node
        else:
            self.value = new_node

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        """ check if current value exists then check if current value is equal to target
        if the target is less than the current value then check to see if there is a left value
        if there isn't then return false if there is then you pass the left value into the 
        contains function vice versa for right. at the end you handle the else statement by 
        returning false"""

        if self.value:
            if self.value == target:
                return True
            else:
                if self.value > target:
                    if self.left:
                        return self.left.contains(target)
                    else:
                        return False
                else:
                    if self.right:
                        # return self.right.contains(target)
                        eval = self.right.contains(target)
                        return eval
                    else:
                        return False
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):

        # check if there's a value
        # check if there's a right.value
        # return self.right.get_max ()
        # if there isn't a right value then return self.value

        if self.value:
            if self.right:
                return self.right.get_max()
            else:
                return self.value

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
