class FirstUnique:
    def __init__(self, nums: List[int]):
        self.impossible = set()
        self.unique = dict()
        for n in nums:
            if n not in self.impossible:
                if n in self.unique:
                    del self.unique[n]
                    self.impossible.add(n)
                else:
                    self.unique[n] = None
                
    def showFirstUnique(self) -> int:
        return next(iter(self.unique)) if len(self.unique) > 0 else -1

    def add(self, value: int) -> None:
         if value not in self.impossible:
            if value in self.unique:
                del self.unique[value]
                self.impossible.add(value)
            else:
                self.unique[value] = None

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)