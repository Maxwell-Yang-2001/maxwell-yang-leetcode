class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        descendStartIndex = 0
        prev = nums[size - 1]
        
        for i in range(size - 2, -1, -1):
            if nums[i] < prev:
                descendStartIndex = i + 1
                break
            prev = nums[i]
        
        # largest possible: sort in ascending order
        # [5, 4, 3, 2, 1] -> [1, 2, 3, 4, 5]
        if descendStartIndex == 0:
            nums.reverse()
        # otherwise the target part in descending order
        # [3, 5, 4, 2, 1] -> [4, 1, 2, 3, 5]
        else:
            smallestGreaterIndex = descendStartIndex;
            for i in range(size - 1, descendStartIndex - 1, -1):
                if nums[i] > nums[descendStartIndex - 1]:
                    smallestGreaterIndex = i
                    break
            tmp = nums[descendStartIndex - 1]
            nums[descendStartIndex - 1] = nums[smallestGreaterIndex]
            nums[smallestGreaterIndex] = tmp
            
            for i in range((size - descendStartIndex) // 2):
                tmp = nums[descendStartIndex + i]
                nums[descendStartIndex + i] = nums[size - 1 - i]
                nums[size - 1 - i] = tmp
            
            
        
        