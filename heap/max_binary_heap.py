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
    
    def extractMax(self):
        if not self.heap:
            return None
        
        self.heap[0],self.heap[-1] = self.heap[-1],self.heap[0]
        max_value = self.heap.pop()
        
        parent_idx = 0
        length = len(self.heap)
        ele = self.heap[0]
        
        while True:
            left_child_idx = (2*parent_idx) + 1 
            right_child_idx = (2*parent_idx) + 2
            swap = None
            leftChild = rightChild = None
            
            if left_child_idx < length:
                leftChild = self.heap[left_child_idx]
                if leftChild > ele:
                    swap = left_child_idx
            
            if right_child_idx < length:
                rightChild = self.heap[right_child_idx]
                if ((swap == None and rightChild > ele) or (swap != None and rightChild > leftChild)):
                    swap = right_child_idx
                
            if not swap: break
            self.heap[parent_idx] = self.heap[swap]
            self.heap[swap] = ele
            parent_idx = swap
        
        return max_value
            
        
        


heap = Max_binary_heap()
heap.insert(4)
heap.insert(7)
heap.insert(20)
heap.insert(23)
heap.insert(2)
heap.extractMax()