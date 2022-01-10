class RandomizedSet:

    def __init__(self):
        self.numDict = dict()
        self.numList = list()

    def insert(self, val: int) -> bool:
        if val not in self.numDict:
            self.numList.append(val)
            self.numDict[val] = len(self.numDict)
            return True
        return False
    
    def remove(self, val: int) -> bool:
        if val in self.numDict:
            index = self.numDict[val]
            lastIndex = len(self.numList) - 1
            
             # swap 2 indices
            tmp = self.numList[lastIndex]
            self.numList[lastIndex] = self.numList[index]
            self.numList[index] = tmp
            
            val = self.numList.pop()
            del self.numDict[val]
            if lastIndex != index:
                self.numDict[tmp] = index
            return True
        return False
    
    def getRandom(self) -> int:
        index = random.randint(0, len(self.numList) - 1)
        
        return self.numList[index]
            

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()