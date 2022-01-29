class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        patterns = dict()
        for string in strings:
            curr_pattern = 0
            for i in range(len(string) - 1):
                curr_pattern = curr_pattern * 27 + 1 + (26 + ord(string[i + 1]) - ord(string[i])) % 26
            if curr_pattern not in patterns:
                patterns[curr_pattern] = []
            patterns[curr_pattern].append(string)
        
        return list(patterns.values())