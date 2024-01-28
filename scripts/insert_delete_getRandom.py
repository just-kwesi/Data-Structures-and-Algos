class RandomizedSet:

    def __init__(self):
        self.obj = {}
        self.arr = []
        

    def insert(self, val: int) -> bool:
        if self.obj.get(val) == None:
            self.obj[val] = len(self.arr)
            return True
        
        return False 

    def remove(self, val: int) -> bool:
        pass

    def getRandom(self) -> int:
        pass
    

obj = RandomizedSet();
obj.insert(9)
print(obj.arr,obj.obj)