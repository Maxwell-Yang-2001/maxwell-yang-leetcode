class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        if n == 0:
            return False
        start, end = 0, n - 1
        
        while start <= end:
            mid = start + (end - start) // 2
            
            if nums[mid] == target:
                return True
        
            if nums[start] == nums[mid]:
                start += 1
                continue
            
            pivot_array = nums[start] <= nums[mid]
            target_array = nums[start] <= target
            
            if pivot_array != target_array:
                if pivot_array:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            
        return False