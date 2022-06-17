class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def connected(prev: str, curr: str) -> bool:
            found_diff = False
            i, limit = 0, len(prev)
            while i < limit:
                if prev[i] != curr[i + (1 if found_diff else 0)]:
                    if found_diff:
                        return False
                    found_diff = True
                    i -= 1
                i += 1
            return True
            
        word_map = [set() for i in range(16)]
        len_list = [1] * len(words)
        
        for i, word in enumerate(words):
            word_map[len(word) - 1].add((word, i))
        
        result = 1
        for curr_len in range(1, 16):
            for curr_word, curr_i in word_map[curr_len]:
                max_curr_len = 1
                for prev_word, prev_i in word_map[curr_len - 1]:
                    prev_chain_len = len_list[prev_i]
                    if max_curr_len <= prev_chain_len and connected(prev_word, curr_word):
                        max_curr_len = 1 + prev_chain_len
                len_list[curr_i] = max_curr_len
                result = max(result, max_curr_len)

        return result