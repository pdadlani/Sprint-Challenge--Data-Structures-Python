class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  # Insert the given value into the tree
  def insert(self, value):
    # check: if the tree is empty
    if self.value is None:
      # then put node at the root
      self.value = BinarySearchTree(value)
      return

    # otherwise
    # if value of new node < value of root 
    if value < self.value:
      # call insert on the left bst, if there is one; 
      # otherwise instantiate a new BST with this value
      if self.left is None:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    # else if value of new node is >= value of root
    # there is no need to actually check this, but it's nice
    elif value >= self.value:
      # call insert on the right bst, if there is one
      # otherwise, instantiate a new BST with this value
      if self.right is None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  # Return True if the tree contains the value
  # False if it does not
  def contains(self, target):
    # if node.value == target:
    if self.value == target:
      # return true
      return True
    # otherwise, if target is < node.value AND there is a left:
    elif target < self.value and self.left:
      # find the target on left bst
      return self.left.contains(target)
    # else if target is >= node.value AND there is a right:
    elif target > self.value and self.right:
      # find the target on the right bst
      return self.right.contains(target)
    return False