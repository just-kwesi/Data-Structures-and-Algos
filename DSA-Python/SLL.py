class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
        
class SinglyLinkedlist:
    def __init__(self) -> None:
        self.head,self.tail = None,None
        self.size = 0
    
    def append(self,data):
        new_node = Node(data)
        
        if self.head == None:
            self.head,self.tail = new_node,new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1
        return self
    
    def prepend(self,data):
        new_node = Node(data)
        
        if self.head == None:
            self.head,self.tail = new_node,new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.size += 1
        return self

    def insert(self,data,index):
        if index >= self.size:
            return self.append(data)
        elif index == 0:
            return self.prepend(data)
        
        new_node = Node(data)
        node_to_change = self.traverseToIndex(index-1)
        
        new_node.next = node_to_change.next
        node_to_change.next = new_node
        self.size += 1
        
        return self
        
    def traverseToIndex(self,index):
        current_node = self.head
        counter = 0
        
        while counter != index:
            current_node = current_node.next
            counter += 1
            
        return current_node
    
    def remove(self,index):
        if index >= self.size or index < 0 :
            return self
        
        if self.size == 1:
            self.head,self.tail = None,None
        elif index == 0:
            self.head = self.head.next
        else:
            preceeding_node = self.traverseToIndex(index-1)
            node_to_remove = preceeding_node.next
            
            if node_to_remove == self.tail:
                preceeding_node.next = None
                self.tail = preceeding_node
            else:
                preceeding_node.next = node_to_remove.next
        
        self.size -= 1
        return self
    
    def printList(self) :
        linked_list_array = []
        current_node = self.head
        while current_node != None:
            linked_list_array.append(current_node.data)
            current_node = current_node.next
        return linked_list_array
    
    def reverse(self):
        if self.head.next == None:
            return self
        
        first = self.head
        second = first.next
        
        while(second) :
            temp = second.next
            second.next = first
            first = second
            second = temp
        
        temp = self.tail
        self.tail = self.head
        self.head = temp
        self.tail.next = None
        
        return self
           
            
        


linked_list = SinglyLinkedlist()
linked_list.append("first").prepend("new first").insert("middle",1).remove(1).append("another")
print(linked_list.printList())
print(linked_list.reverse().printList())