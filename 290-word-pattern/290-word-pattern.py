class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_dict = dict()
        s = ' ' + s + ' '
        space = 0
        
        for i in range(len(pattern)):
            next_space = s.find(' ', space + 1)
            if next_space == -1:
                return False
            word = s[space + 1 : next_space]
            if pattern[i] in pattern_dict:
                if pattern_dict[pattern[i]] != word:
                    return False
            else:
                pattern_dict[pattern[i]] = word
            space = next_space
        
        return s.find(' ', space +1) == -1 and len(set(pattern_dict.values())) == len(pattern_dict)
        