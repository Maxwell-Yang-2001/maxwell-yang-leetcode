class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        words1_dict_list = [[0] * 26 for i in range(len(words1))]
        max_words2_dict = [0] * 26

        ord_a = ord('a')
        for i, word in enumerate(words1):
            for c in word:
                words1_dict_list[i][ord(c) - ord_a] += 1
        
        curr_words2_dict = [0] * 26
        for i, word in enumerate(words2):
            for c in word:
                curr_words2_dict[ord(c) - ord_a] += 1
            for j in range(26):
                max_words2_dict[j] = max(max_words2_dict[j], curr_words2_dict[j])
                curr_words2_dict[j] = 0
        
        result = []
        for i in range(len(words1)):
            universal = True
            for j in range(26):
                if words1_dict_list[i][j] < max_words2_dict[j]:
                    universal = False
                    break
            if universal:
                result.append(words1[i])
        
        return result