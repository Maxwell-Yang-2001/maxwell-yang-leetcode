class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        l = len(arr)
        if l < 3:
            return False
        
        ascend = True
        for i in range(l - 1):
            if arr[i] == arr[i + 1]:
                return False
            elif arr[i] < arr[i + 1]:
                if not ascend:
                    return False
            else:
                if ascend:
                    if i == 0:
                        return False
                    ascend = False
        
        # return false if never descended
        return not ascend
            