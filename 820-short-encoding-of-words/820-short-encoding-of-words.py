class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        # construct a Trie
        Trie = lambda: collections.defaultdict(Trie)
        
        trie = Trie()
        for w in words:
            curr = trie
            for c in w[::-1]:
                curr = curr[c]
        
        # sum of the depth of all leaves: dfs
        def dfs(trie: Trie, depth: int) -> int:
            if len(trie) == 0:
                return depth
            result = 0
            for k in trie:
                result += dfs(trie[k], depth + 1)
            return result
        
        return dfs(trie, 1)
            
        
        