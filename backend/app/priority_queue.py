import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []
    
    def push(self, item, priority):
        heapq.heappush(self.heap, (priority, item))
    
    def pop(self):
        return heapq.heappop(self.heap)[1]
    
    def is_empty(self):
        return len(self.heap) == 0
    
    def peek(self):
        return self.heap[0][1] if not self.is_empty() else None
