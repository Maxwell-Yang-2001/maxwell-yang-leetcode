class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        arr_dict = {num: 0 for num in arr}
        
        result = 0
        for i, num in enumerate(arr):
            # each number could be a leaf
            curr = 1
            for j in range(i):
                if arr[j] > num ** 0.5:
                    break
                if num % arr[j] == 0 and (num // arr[j]) in arr_dict:
                    # square case: add once; non-square case: add twice
                    multiplier = 1 if num == arr[j] * arr[j] else 2
                        
                    curr += arr_dict[arr[j]] * arr_dict[num // arr[j]] * multiplier
            
            arr_dict[num] = curr
            result += curr
        
        return result % (10 ** 9 + 7)