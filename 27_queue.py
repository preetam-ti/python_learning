"""https://www.geeksforgeeks.org/queue-in-python/"""

"""
Like stack, queue is a linear data structure that stores items in First In First Out (FIFO) manner.
 With a queue the least recently added item is removed first. A good example of queue is any queue 
 of consumers for a resource where the consumer that came first is served first.

Operations associated with queue are: 
 

Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition – Time Complexity : O(1)
Dequeue: Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to be an Underflow condition – Time Complexity : O(1)
Front: Get the front item from queue – Time Complexity : O(1)
Rear: Get the last item from queue – Time Complexity : O(1)

Implementation
There are various ways to implement a queue in Python. This article covers the implementation of queue using data structures and modules from Python library.
Queue in Python can be implemented by the following ways:
 

list
collections.deque
queue.Queue


Implementation using list
List is a Python’s built-in data structure that can be used as a queue. Instead of enqueue() and 
dequeue(), append() and pop() function is used. However, lists are quite slow for this purpose 
because inserting or deleting an element at the beginning requires shifting all of the other elements
 by one, requiring O(n) time.

 # Python program to 
# demonstrate queue implementation
# using list
  
# Initializing a queue
queue = []
  
# Adding elements to the queue
queue.append('a')
queue.append('b')
queue.append('c')
  
print("Initial queue")
print(queue)
  
# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
  
print("\nQueue after removing elements")
print(queue)
  
# Uncommenting print(queue.pop(0))
# will raise and IndexError
# as the queue is now empty



#########
Implementation using collections.deque
Queue in Python can be implemented using deque class from the collections module. Deque is preferred 
over list in the cases where we need quicker append and pop operations from both the ends of container,
 as deque provides an O(1) time complexity for append and pop operations as compared to list which 
 provides O(n) time complexity. Instead of enqueue and deque, append() and popleft() functions are
  used.


# Python program to
# demonstrate queue implementation
# using collections.dequeue
  
  
from collections import deque
  
# Initializing a queue
q = deque()
  
# Adding elements to a queue
q.append('a')
q.append('b')
q.append('c')
  
print("Initial queue")
print(q)
  
# Removing elements from a queue
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())
  
print("\nQueue after removing elements")
print(q)
  
# Uncommenting q.popleft()
# will raise an IndexError
# as queue is now empty

##########
Implementation using queue.Queue

# Python program to
# demonstrate implementation of
# queue using queue module
  
  
from queue import Queue
  
# Initializing a queue
q = Queue(maxsize = 3)
  
# qsize() give the maxsize 
# of the Queue 
print(q.qsize()) 
  
# Adding of element to queue
q.put('a')
q.put('b')
q.put('c')
  
# Return Boolean for Full 
# Queue 
print("\nFull: ", q.full()) 
  
# Removing element from queue
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())
  
# Return Boolean for Empty 
# Queue 
print("\nEmpty: ", q.empty())
  
q.put(1)
print("\nEmpty: ", q.empty()) 
print("Full: ", q.full())
  
# This would result into Infinite 
# Loop as the Queue is empty. 
# print(q.get())


"""

"""

In the previous post, we introduced Queue and discussed array implementation. In this post, linked list implementation is discussed. The following two main operations must be implemented efficiently.

In a Queue data structure, we maintain two pointers, front and rear. The front points the first item of queue and rear points to last item.

enQueue() This operation adds a new node after rear and moves rear to the next node.
deQueue() This operation removes the front node and moves front to the next node.



# Python3 program to demonstrate linked list
# based implementation of queue
  
# A linked list (LL) node
# to store a queue entry
class Node:
      
    def __init__(self, data):
        self.data = data
        self.next = None
  
# A class to represent a queue
  
# The queue, front stores the front node
# of LL and rear stores the last node of LL
class Queue:
      
    def __init__(self):
        self.front = self.rear = None
  
    def isEmpty(self):
        return self.front == None
      
    # Method to add an item to the queue
    def EnQueue(self, item):
        temp = Node(item)
          
        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp
  
    # Method to remove an item from queue
    def DeQueue(self):
          
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next
  
        if(self.front == None):
            self.rear = None
  
# Driver Code
if __name__== '__main__':
    q = Queue()
    q.EnQueue(10)
    q.EnQueue(20)
    q.DeQueue()
    q.DeQueue()
    q.EnQueue(30)
    q.EnQueue(40)
    q.EnQueue(50) 
    q.DeQueue()   
    print("Queue Front " + str(q.front.data))
    print("Queue Rear " + str(q.rear.data))

"""