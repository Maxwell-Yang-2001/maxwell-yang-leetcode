class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.y = 0
        self.x = 0
        self.vec = []
        for row in vec:
            if len(row) != 0:
                self.vec.append(row)

    def next(self) -> int:
        result = self.vec[self.y][self.x]
        self.x += 1
        if self.x == len(self.vec[self.y]):
            self.x = 0
            self.y += 1
        return result

    def hasNext(self) -> bool:
        return len(self.vec) > self.y and len(self.vec[self.y]) > self.x;


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()