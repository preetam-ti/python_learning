""""
Priority Queues are abstract data structures where each data/value in the queue has a certain priority.
 For example, In airlines, baggage with the title “Business” or “First-class” arrives earlier than 
 the rest. Priority Queue is an extension of the queue with the following properties.

An element with high priority is dequeued before an element with low priority.
If two elements have the same priority, they are served according to their order in the queue.

arious applications of the Priority queue in Computer Science are:
Job Scheduling algorithms, CPU and Disk Scheduling, managing resources that are shared among 
different processes, etc.

"""
# A simple implementation of Priority Queue
# using Queue.
class PriorityQueue(object):
    def __init__(self):
        self.queue = []
  
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
  
    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0
  
    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)
  
    # for popping an element based on Priority
    def delete(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()
  
if __name__ == '__main__':
    myQueue = PriorityQueue()
    myQueue.insert(12)
    myQueue.insert(1)
    myQueue.insert(14)
    myQueue.insert(7)
    print(myQueue)        
    while not myQueue.isEmpty():
        print(myQueue.delete())