class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l = len(nums)
        k %= l
        
        # compute gcd
        gcd = 0
        num1 = l
        num2 = k
        while num2 != 0:
            num1, num2 = num2, num1 % num2
        gcd = num1
        
        for i in range(gcd):
            curr_i = (i + k) % l
            curr = nums[i]
            while curr_i != i:
                save = nums[curr_i]
                nums[curr_i] = curr
                curr = save
                curr_i = (curr_i + k) % l
            nums[i] = curr