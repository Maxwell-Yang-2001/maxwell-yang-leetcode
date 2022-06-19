class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        Trie = lambda: collections.defaultdict(Trie)
        
        trie = Trie()
        
        for p in products:
            curr_trie = trie
            for c in p:
                curr_trie = curr_trie[c]
            # A indicate end of a word
            curr_trie['A'] = 1
        
        result = []
        curr_word = ''
        curr_list = None
        def dfs(trie: Trie, path: str):
            if len(curr_list) == 3:
                return
            
            if len(trie) == 0:
                if path != curr_word:
                    curr_list.append(path)
            else:
                keys = list(trie.keys())
                keys.sort()
                if keys[0] == 'A':
                    curr_list.append(path)
                    keys = keys[1:]
                for k in keys:
                    dfs(trie[k], path + k)
            
        curr_trie = trie
        for c in searchWord:
            curr_list = []
            curr_trie = curr_trie[c]
            curr_word += c
            if len(curr_trie) == 0:
                result.append(curr_list)
                break
            dfs(curr_trie, curr_word)
            if len(curr_list) < 3:
                result.append(curr_list)
                break
            result.append(curr_list)
        
        for i in range(len(curr_word), len(searchWord)):
            new_list = []
            for curr_word in curr_list:
                if len(curr_word) > i and curr_word[i] == searchWord[i]:
                    new_list.append(curr_word)
            result.append(new_list)
            curr_list = new_list
        return result
        