"""
	Playing with linked lists.
	
	Created class Node for instantiating nodes of single-linked lists.
	
	Created class LinkedList for instantiating linked lists,
	calculating their length, and performing the following functions:
	* prepending a node;
	* reversing the list (2 implementations);
	* printing the list;
	* printing the list in a reverse (end to head) order.
	
    main() is using the above classes to create a list with 3 nodes, prepends
	one more node, prints the list, reverses the list, prints it second time,
	prints it in reverse order, again reverses it, and prints it the 4th time.
"""
#import pdb

class Node: 
  def __init__(self, cargo = None, nextNode = None): 
    self.cargo = cargo 
    self.next  = nextNode 

  def __str__(self): 
    return str(self.cargo) 

class LinkedList:
  def __init__(self, head):
    self.head = head
    current = head
    length = 1
    while (current.next is not None):
      length += 1
      current = current.next
    self.length = length

    # Function to prepend a node with cargo 'cargo' to the linked list
  def addNode(self, cargo):
    node = Node(cargo)
    node.next = self.head
    self.head = node
    self.length += 1

  # Function to reverse the linked list
  def reverse(self):
    prev = self.head
    if prev.next:
      current = prev.next
    else:
      print("Nothing to reverse: there is only 1 node in the list.")
      return self.head
    while (current.next is not None):
      next = current.next
      current.next = prev
      prev = current
      current = next
    current.next = prev
    self.head.next = None # mutates "next" attribute of callee's node,
                          # which was passed as "head"
    self.head = current   # changes self.head to refer to a new object
    return self.head

  # Another function to reverse the linked list
  def reverse2(self):
    prev = None
    current = self.head
    while current:
      next = current.next
      current.next = prev
      prev = current
      current = next
    self.head = prev
    return self.head

  # Function to print linked lists starting at the node 'node'
  def printList(self, node):
    while (node is not None):
      print(node)
      node = node.next
    print

  # Recursive function to print linked lists starting at the node 'list'
  def printBackward(self, list):
    if list == None: return
    head = list
    tail = list.next
    self.printBackward(tail)
    print(head)

if __name__ == "__main__":
  # creating a single-linked list with 3 nodes: 11 -> 22 -> 33
  node1 = Node(11)
  node2 = Node(22)
  node3 = Node(33)
  node1.next = node2
  node2.next = node3
  # creating an object "ll" for the above linked list
  ll = LinkedList(node1)
  # prepending one more node to the list
  ll.addNode('zerozero')
  print("\nInnitial list:")
  ll.printList(ll.head)
  # reversing the list
  ll.reverse()
  print("\nReversed list:")
  ll.printList(ll.head)
  print("\nReversed list printed in reverse order:")
  ll.printBackward(ll.head)
  # reversing the list once again
  ll.reverse2()
  print("\nReversed x2 list:")
  ll.printList(ll.head)  
  
