class Node:
  def __init__(self, data, next):
      self.data = data
      self.next = next or None

class LinkedList:
  def __init__(self):
      self.head = None

  def append(self, data):
      new_node = Node(data)
      if self.head is None:
          self.head = new_node
      else:
          current = self.head
          while current.next:
              current = current.next
          current.next = new_node

  def display(self):
      current = self.head
      while current:
          print(current.data, end=" ")
          current = current.next

  def remove(self, key):
      current = self.head
      prev = None
      while current:
          if current.data == key:
              if prev:
                  prev.next = current.next
              else:
                  self.head = current.next
              return
          prev = current
          current = current.next

  def reverse(self):
      current = self.head
      prev = None
      while current:
          next_node = current.next
          current.next = prev
          prev = current
          current = next_node
      self.head = prev

# Create a linked list
my_list = LinkedList()

#### Prompt
# given non-emtpy linked lists whcih consist of a positive integer. The digits are 
# stored in reverse order, and each node contains one digit

"""
input1 --> [2-> 4-> 3], input2 --> [5 -> 6 -> 4]
output1 --> [7 -> 0 -> 8]

step 1: evaluate node from each list and sum them up
if there is > 10, carry over 1 to the next value

"""

def addTwoNumbers(l1, l2):
  """
  l1: linked list with numbers in reverse
  l2: linked list with numbers in reverse
  output: summed version of l1 + l2
  """
  dummy = Node(None, None)
  currNode = dummy
  carry = 0

  while(l1 or l2 or carry):
    sum = l1.data + l2.data + carry
    carry = sum // 10
    
    sum %= 10
    currNode.next = Node(sum, None)
    currNode = currNode.next
    
    l1 = l1.next
    l2 = l2.next
  
  return dummy.next

summedList = addTwoNumbers(Node(2, Node(4, Node(3, None))), Node(5, Node(6, Node(4, None))))

while summedList:
  print(summedList.data)
  summedList = summedList.next