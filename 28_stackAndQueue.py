"""
In case of stack, list implementation works fine and provides both append() and pop() in O(1) time. When we use deque implementation, we get same time complexity.
"""
# Python code to demonstrate Implementing 
# Stack using deque
from collections import deque
queue = deque(["Ram", "Tarun", "Asif", "John"])
print(queue)
queue.append("Akbar")
print(queue)
queue.append("Birbal")
print(queue)
print(queue.pop())                 
print(queue.pop())                 
print(queue)

"""
But when it comes to queue, the above list implementation is not efficient. In queue when pop() is made from the beginning of the list which is slow. This occurs due to the properties of list, which is fast at the end operations but slow at the beginning operations, as all other elements have to be shifted one by one.
So, we prefer the use of dequeue over list, which was specially designed to have fast appends and pops from both the front and back end.

Let’s look at an example and try to understand queue using collections.deque:
"""

# Python code to demonstrate Implementing 
# Queue using deque
from collections import deque
queue = deque(["Ram", "Tarun", "Asif", "John"])
print(queue)
queue.append("Akbar")
print(queue)
queue.append("Birbal")
print(queue)
print(queue.popleft())                 
print(queue.popleft())                 
print(queue)

