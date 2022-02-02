class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        occurence_dict = dict()
        
        for i in arr:
            if i in occurence_dict:
                occurence_dict[i] += 1
            else:
                occurence_dict[i] = 1
        
        occurence_list = list(occurence_dict.values())
        occurence_list.sort(reverse=True)
        
        target = len(arr) // 2
        for i, o in enumerate(occurence_list):
            target -= o
            if target <= 0:
                return i + 1
        
        return -1