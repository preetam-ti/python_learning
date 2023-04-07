"""
Circular linked list is a linked list where all nodes are connected to form a circle. There is no 
NULL at the end. A circular linked list can be a singly circular linked list or doubly circular 
linked list.


Advantages of Circular Linked Lists:
1) Any node can be a starting point. We can traverse the whole list by starting from any point. 
We just need to stop when the first visited node is visited again.

2) Useful for implementation of queue. Unlike this implementation, we don’t need to maintain two 
pointers for front and rear if we use circular linked list. We can maintain a pointer to the last
 inserted node and front can always be obtained as next of last.

3) Circular lists are useful in applications to repeatedly go around the list. For example, when 
multiple applications are running on a PC, it is common for the operating system to put the 
running applications on a list and then to cycle through them, giving each of them a slice of 
time to execute, and then making them wait while the CPU is given to another application. 
It is convenient for the operating system to use a circular list so that when it reaches the
 end of the list it can cycle around to the front of the list.

4)Circular Doubly Linked Lists are used for implementation of advanced data structures like Fibonacci Heap.
"""


# Python program to demonstrate
# circular linked list traversal
 
# Structure for a Node
class Node:
     
    # Constructor to create  a new node
    def __init__(self, data):
        self.data = data
        self.next = None
 
class CircularLinkedList:
     
    # Constructor to create a empty circular linked list
    def __init__(self):
        self.head = None
 
    # Function to insert a node at the beginning of a
    # circular linked list
    def push(self, data):
        ptr1 = Node(data)
        temp = self.head
         
        ptr1.next = self.head
 
        # If linked list is not None then set the next of
        # last node
        if self.head is not None:
            while(temp.next != self.head):
                temp = temp.next
            temp.next = ptr1
 
        else:
            ptr1.next = ptr1 # For the first node
 
        self.head = ptr1
 
    # Function to print nodes in a given circular linked list
    def printList(self):
        temp = self.head
        if self.head is not None:
            while(True):
                print (temp.data, end=" ")
                temp = temp.next
                if (temp == self.head):
                    break
 
 
# Driver program to test above function
 
# Initialize list as empty
cllist = CircularLinkedList()
 
# Created linked list will be 11->2->56->12
cllist.push(12)
cllist.push(56)
cllist.push(2)
cllist.push(11)
 
print ("Contents of circular Linked List")
cllist.printList()

"""
Time Complexity: O(n) As we need to move through the whole list
Auxiliary Space: O(1) As no extra space is used
"""


"""Deletion from Circular Linked List"""

"""
# Python program to delete a given key from
# linked list.
  
# Node of a doubly linked list 
class Node: 
    def __init__(self, next = None, data = None): 
        self.next = next
        self.data = data 
  
# Function to insert a node at the beginning of 
# a Circular linked list 
def push(head_ref, data):
  
    # Create a new node and make head as next
    # of it.
    ptr1 = Node()
    ptr1.data = data
    ptr1.next = head_ref
  
    # If linked list is not None then set the 
    # next of last node 
    if (head_ref != None) :
          
        # Find the node before head and update
        # next of it.
        temp = head_ref
        while (temp.next != head_ref):
            temp = temp.next
        temp.next = ptr1
      
    else:
        ptr1.next = ptr1 # For the first node 
  
    head_ref = ptr1
    return head_ref
  
# Function to print nodes in a given 
# circular linked list 
def printList( head):
  
    temp = head
    if (head != None) :
        while(True) :
            print( temp.data, end = " ")
            temp = temp.next
            if (temp == head):
                break
    print()
  
# Function to delete a given node from the list 
def deleteNode( head, key) :
  
    # If linked list is empty
    if (head == None):
        return
          
    # If the list contains only a single node
    if((head).data == key and (head).next == head):
      
        head = None
      
    last = head
    d = None
      
    # If head is to be deleted
    if((head).data == key) :
          
        # Find the last node of the list
        while(last.next != head):
            last = last.next
              
        # Point last node to the next of head i.e. 
        # the second node of the list
        last.next = (head).next
        head = last.next
      
    # Either the node to be deleted is not found 
    # or the end of list is not reached
    while(last.next != head and last.next.data != key) :
        last = last.next
  
    # If node to be deleted was found
    if(last.next.data == key) :
        d = last.next
        last.next = d.next
      
    else:
        print("no such keyfound")
      
    return head
  
# Driver code
  
# Initialize lists as empty 
head = None
  
# Created linked list will be 2.5.7.8.10 
head = push(head, 2)
head = push(head, 5)
head = push(head, 7)
head = push(head, 8)
head = push(head, 10)
  
print("List Before Deletion: ")
printList(head)
  
head = deleteNode(head, 7)
  
print( "List After Deletion: ")
printList(head)"""

"""https://www.geeksforgeeks.org/convert-singly-linked-list-circular-linked-list/?ref=lbp"""