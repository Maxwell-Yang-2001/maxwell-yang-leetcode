# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        numSet = set(nums)
        
        groups = 0
        isGap = True
        while head != None:
            if head.val in nums:
                if isGap:
                    isGap = False
                    groups += 1
            else:
                if not isGap:
                    isGap = True
            head = head.next
        
        return groups