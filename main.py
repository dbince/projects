from collections import deque

class Node:

  def __init__(self, value):
    self.left = None
    self.right = None
    self.frequency = 1
    self.value = value


class BinarySearchTree:

  def __init__(self):
    self.root = None

  def insert(self, value):
    if self.root:
      self.insert_into_tree(self.root, value)
    else:
      self.root = Node(value)

  def insert_into_tree(self, node, value):
    if value < node.value:
      # if less, then going to left
      if node.left:
        self.insert_into_tree(node.left, value)
      else:
        node.left = Node(value)
    elif value > node.value:
      if node.right:
        self.insert_into_tree(node.right, value)
      else:
        node.right = Node(value)

  def inorder_traversal(self):
    result = []
    self.inorder_traversal_recursion(self.root, result)
    return result

  def inorder_traversal_recursion(self, node, result):
    if node:
      self.inorder_traversal_recursion(node.left, result)
      result.append(node.value)
      self.inorder_traversal_recursion(node.right, result)

  def preorder_traversal(self):
    result = []
    self.preorder_traversal_recursion(self.root, result)
    return result

  def preorder_traversal_recursion(self, node, result):
    if node:
      result.append(node.value)
      self.preorder_traversal_recursion(node.left, result)
      self.preorder_traversal_recursion(node.right, result)

  def postorder_traversal(self):
    result = []
    self.postorder_traversal_recursion(self.root, result)
    return result

  def postorder_traversal_recursion(self, node, result):
    if node:
      self.postorder_traversal_recursion(node.left, result)
      self.postorder_traversal_recursion(node.right, result)
      result.append(node.value)


bst = BinarySearchTree()
bst.insert(4)
bst.insert(2)
bst.insert(10)
bst.insert(1)
bst.insert(3)
bst.insert(9)
bst.insert(14)
bst.insert(11)
bst.insert(15)

# print(bst.inorder_traversal())
# print(bst.postorder_traversal())
# print(bst.preorder_traversal())

# for swapping:
"""
temp = node.left
node.left = node.right
node.right = temp
"""


def reflectTree(node):
  if not node:
    return node

  reflectTree(node.left)
  reflectTree(node.right)

  if node.right and node.left:
    print(f"Switching nodes: {node.left.value} <--> {node.right.value}")

  temp = node.right
  node.right = node.left
  node.left = temp
  if (node.right and node.left):
    print(f"Switched nodes: {node.left.value} <--> {node.right.value}")
  return node


# print(reflectTree(bst.root))

def level_order_traversal(root):
  """
  input: the root of the tree
  output: list arrays with the values in each level
  example 1
  input: [3, 6, 7, 8, 9, 10]
  output: [[3], [6, 7], [9, 10]]
  example 2
  input: [3]
  output: [[3]]
  example 3
  input: []
  output: []

  Breadth first search
  """
  if not root:
    return []
    
  levels = []
  queue = deque([root])
  
  while queue:
    cur_level_size = len(queue)
    cur_level = []

    for i in range(cur_level_size):
      first_node = queue.popleft()
      cur_level.append(first_node.value)

      # need to add left and right of first_node
      # where do we add it? queue
      if first_node.left:
        queue.append(first_node.left)
      if first_node.right:
        queue.append(first_node.right)
        
    levels.append(cur_level)
  
  return levels

bst = BinarySearchTree()
bst.insert(4)
bst.insert(2)
bst.insert(10)
bst.insert(1)
bst.insert(3)
bst.insert(9)
bst.insert(14)
bst.insert(11)
bst.insert(15)

# print(level_order_traversal(bst.root))

# DFS --> depth first search

# [-10, -3, 0, 5, 9] --> turn it into a tree

#      0
#   -3   9
# -10   5

def arrayToBST(sortedNums):
  if len(sortedNums) == 0:
    return None

  
  middle_index = len(sortedNums)//2
  middle = sortedNums[middle_index]
  root = Node(middle)
  left_subarray = sortedNums[:middle_index]
  right_subarray = sortedNums[middle_index + 1:]
  root.left = arrayToBST(left_subarray)
  root.right = arrayToBST(right_subarray)

  return root

nums = [-10, -3, 0, 5, 9]
BSTRoot = arrayToBST([-10, -3, 0, 5, 9])
