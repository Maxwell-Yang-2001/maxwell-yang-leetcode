class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        curr_count, curr_char = 0, ' '
        s_pattern, w_pattern = [], []
        
        # record pattern of s
        for c in s:
            if c != curr_char:
                if curr_count != 0:
                    s_pattern.append((curr_count, curr_char))
                curr_char = c
                curr_count = 1
            else:
                curr_count += 1
        
        s_pattern.append((curr_count, curr_char))
        
        result = 0
        for w in words:
            
            curr_count, curr_char = 0, ' '
            w_pattern.clear()
            
            # record pattern of w
            for c in w:
                if c != curr_char:
                    if curr_count != 0:
                        w_pattern.append((curr_count, curr_char))
                    curr_char = c
                    curr_count = 1
                else:
                    curr_count += 1
            
            w_pattern.append((curr_count, curr_char))
            
            if len(s_pattern) != len(w_pattern):
                continue
            
            mismatch = False
            for i in range(len(s_pattern)):
                if s_pattern[i][1] != w_pattern[i][1]:
                    mismatch = True
                    break
                if s_pattern[i][0] < w_pattern[i][0] or (s_pattern[i][0] > w_pattern[i][0] and s_pattern[i][0] < 3):
                    mismatch = True
                    break
            
            if not mismatch:
                result += 1
        
        return result
            