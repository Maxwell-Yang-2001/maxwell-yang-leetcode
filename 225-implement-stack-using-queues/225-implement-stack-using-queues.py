class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q1.insert(0, x)

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.insert(0, self.q1.pop())
        tmp = self.q1
        self.q1 = self.q2
        self.q2 = tmp
        return self.q2.pop()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return not bool(self.q1)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()