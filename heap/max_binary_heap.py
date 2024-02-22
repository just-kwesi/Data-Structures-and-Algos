class Max_binary_heap:
    def __init__(self) -> None:
        self.heap = []
    
    def insert(self,value):
        self.heap.append(value)
       
        idx = len(self.heap) - 1
        parent_idx = (idx-1)//2
       
        while parent_idx >= 0 and (self.heap[parent_idx] < self.heap[idx]):
           self.heap[parent_idx],self.heap[idx] = self.heap[idx], self.heap[parent_idx]
           
           idx = parent_idx
           parent_idx = (idx-1)//2
           
        print(self.heap)


heap = Max_binary_heap()
heap.insert(4)
heap.insert(7)
heap.insert(20)
heap.insert(23)
heap.insert(2)