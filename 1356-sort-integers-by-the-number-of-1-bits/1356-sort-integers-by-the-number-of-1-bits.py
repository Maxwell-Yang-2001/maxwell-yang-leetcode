class Solution:
    def getKey(self, i: int) -> int:
        copy = i
        key = 0
        while i > 0:
            key += i % 2
            i //= 2
        key = 100000 * key + copy
        return key
        
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key= self.getKey)
        return arr