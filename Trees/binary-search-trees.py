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
            if cur.value == value: return cur
            elif cur.value > value: cur= cur.left
            else: cur = cur.right
        
        return False

    def findParent(self,value):
        if not self.root: return False
        
        cur = self.root
        prev = None
        
        while cur:
            if cur.value == value: return prev
            elif cur.value > value: 
                prev = cur
                cur = cur.left
            else:
                prev = cur 
                cur = cur.right
        
        return False
    
    def findSuccessor(self,node):
        if not node.left:
            return node

    def remove(self,value):
        # find the node to to reomove
        nodeToRemove = self.find(value)
        if not nodeToRemove: return False
        
        # replace it with it's successor
        parent = self.findParent(value)
        
        # remove if it's a leaf node
        if not nodeToRemove.left and not nodeToRemove.right:
            # remove the leaf
            if parent.left == nodeToRemove:
                parent.left = None
            else:
                parent.right = None
        # if it only has a right child then just bypass node
        elif not nodeToRemove.left and nodeToRemove.right:
            if parent.left == nodeToRemove:
                parent.left = nodeToRemove.right
            else:
                parent.right = nodeToRemove.right
        
        # if it only has a left child then just bypass 
        elif nodeToRemove.left and not nodeToRemove.right:
            if parent.left == nodeToRemove:
                parent.left = nodeToRemove.left
            else:
                parent.right = nodeToRemove.left
        
        # if it has all children find the successor and replace node with it
        # successor is the smallest value greater than the node in the tree
        else:
            self.findSuccessor(nodeToRemove)
            
        
        
    


bst = BinarySearchTree()
bst.insert(6)
bst.insert(2)
bst.insert(7)
bst.insert(4)
bst.insert(8)
bst.insert(5)


print(bst.find(6))