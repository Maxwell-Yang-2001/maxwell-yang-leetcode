def bSearchLeft(values: List[int], left: int, right: int, val: int) -> int:
    if left > right:
        return left
    mid = (left + right) // 2
    if values[mid] == val:
        return mid
    elif values[mid] < val:
        return bSearchLeft(values, mid + 1, right, val)
    else:
        return bSearchLeft(values, left, mid - 1, val)

def bSearchRight(values: List[int], left: int, right: int, val: int) -> int:
    if left > right:
        return right
    mid = (left + right + 1) // 2
    if values[mid] == val:
        return mid
    elif values[mid] < val:
        return bSearchRight(values, mid + 1, right, val)
    else:
        return bSearchRight(values, left, mid - 1, val)


class RangeFreqQuery:
    freq = None
    def __init__(self, arr: List[int]):
        self.freq = dict()
        for i, a in enumerate(arr):
            if a in self.freq:
                self.freq[a].append(i)
            else:
                self.freq[a] = [i]
    
    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.freq:
            return 0
        occurences = self.freq[value]
        leftIndex = bSearchLeft(occurences, 0, len(occurences) - 1, left)
        
        if leftIndex == len(occurences) - 1 and occurences[leftIndex] < left:
            return 0
        
        rightIndex = bSearchRight(occurences, leftIndex, len(occurences) - 1, right)
        
        if rightIndex == 0 and occurences[rightIndex] > right:
            return 0
        
        return rightIndex - leftIndex + 1
            
                

# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)