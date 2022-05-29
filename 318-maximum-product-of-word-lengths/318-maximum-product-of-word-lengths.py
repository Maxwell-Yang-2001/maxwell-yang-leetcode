class Solution:
    def maxProduct(self, words: List[str]) -> int:
        look_up = defaultdict(lambda: 0)
        ord_a = ord('a')
        for word in words:
            bitmask = 0
            for c in word:
                bitmask |= 2 ** (ord(c) - ord_a)
            look_up[bitmask] = max(look_up[bitmask], len(word))
        
        result = 0
        bitmasks = list(look_up.keys())
        for i in range(len(bitmasks)):
            for j in range(i + 1, len(bitmasks)):
                if bitmasks[i] & bitmasks[j] == 0:
                    result = max(result, look_up[bitmasks[i]] * look_up[bitmasks[j]])
        
        return result
            