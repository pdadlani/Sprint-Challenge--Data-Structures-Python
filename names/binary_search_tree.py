class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # If inserting, we must already have a tree/root
        if self.value is None:
            self.value = value
            return self.value
        # If value is less than self.value, go left, make a new tree/node, if empty. Otherwise, keep going (recursion)
        elif value < self.value:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        # If greater than or equal to self.value, go right, make a new tree/node, if empty. Otherwise, keep going (recursion)
        elif value >= self.value:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if target == self.value, return it
        if target == self.value:
            return True
        # otherwise, go left or right based on smaller or bigger
        elif target > self.value and self.right:
            # move right
            return self.right.contains(target)
        elif target < self.value and self.left:
            # move left
            return self.left.contains(target)
        return False