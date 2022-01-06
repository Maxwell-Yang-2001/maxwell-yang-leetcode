class RevLinkedNode:
    def __init__(self, val: int, before, after):
        self.val = val
        self.before = before
        self.after = after

class MyCircularQueue:
    def __init__(self, k: int):
        self.maxSize = k
        self.size = 0
        self.head = None

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        elif self.isEmpty():
            self.head = RevLinkedNode(value, None, None)
            self.head.before = self.head
            self.head.after = self.head
        else:
            newTail = RevLinkedNode(value, self.head.before, self.head)
            self.head.before.after = newTail
            self.head.before = newTail
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.size == 1:
            self.head = None
        else:
            self.head.before.after = self.head.after
            self.head.after.before = self.head.before
            self.head = self.head.after
        self.size -= 1
        return True
        

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.head.val

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.head.before.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size >= self.maxSize


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()