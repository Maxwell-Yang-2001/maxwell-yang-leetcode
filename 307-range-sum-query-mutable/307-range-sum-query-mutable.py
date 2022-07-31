class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        tree = [0] * (2 * n)
        
        for i in range(0, n):
            tree[i + n] = nums[i]
        
        for i in range(n - 1, -1, -1):
            tree[i] = tree[i * 2] + tree[i * 2 + 1]
        
        self.n = n
        self.tree = tree

    def update(self, index: int, val: int) -> None:
        index += self.n
        self.tree[index] = val
        
        while index > 0:
            left = index
            right = index
            if index % 2 == 0:
                right = index + 1
            else:
                left = index - 1
        
            self.tree[index // 2] = self.tree[left] + self.tree[right]
            index //= 2

    def sumRange(self, left: int, right: int) -> int:
        left += self.n
        right += self.n
        
        sum = 0
        while left <= right:
            if left % 2 == 1:
                sum += self.tree[left]
                left += 1
            if right % 2 == 0:
                sum += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
        return sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)