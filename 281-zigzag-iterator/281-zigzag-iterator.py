class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.order = deque()
        self.collections = [v1, v2]
        if len(v1) > 0:
            self.order.append((0, 0))
        if len(v2) > 0:
            self.order.append((1, 0))

    def next(self) -> int:
        if self.hasNext():
            n = self.order.popleft()
            result = self.collections[n[0]][n[1]]
            if len(self.collections[n[0]]) > n[1] + 1:
                self.order.append((n[0], n[1] + 1))
            return result

    def hasNext(self) -> bool:
        return len(self.order) > 0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())