class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self,value):
        newNode = Node(value)
        if not self.root:
            self.root = newNode
            return self

        cur = self.root
        inserted = False
        while not inserted:
            if value < cur.value:
                if not cur.left:
                    cur.left = newNode
                    inserted = True
                else:
                    cur = cur.left
            else:
                if not cur.right:
                    cur.right =newNode
                    inserted = True
                else:
                    cur = cur.right
        
        return self
    
    def find(self,value):
        if not self.root: return False
        
        cur = self.root
        
        while cur:
            if cur.value == value: return True
            elif cur.value > value: cur= cur.left
            else: cur = cur.right
        
        return False
    


bst = BinarySearchTree()
bst.insert(6)
bst.insert(2)
bst.insert(7)
bst.insert(4)
bst.insert(8)
bst.insert(5)


print(bst.find(6))