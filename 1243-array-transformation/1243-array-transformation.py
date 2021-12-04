class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        add = [0] * len(arr)
        changed = True
        while changed:
            changed = False
            for i in range(1, len(arr) - 1):
                if arr[i - 1] > arr[i] and arr[i] < arr[i + 1]:
                    add[i] += 1
                    changed = True
                elif arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
                    add[i] -= 1
                    changed = True
            for i in range(len(arr)):
                arr[i] += add[i]
                add[i] = 0
        return arr