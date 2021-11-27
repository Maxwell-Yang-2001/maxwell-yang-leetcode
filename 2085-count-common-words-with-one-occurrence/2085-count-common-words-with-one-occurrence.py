class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        result = 0
        words1Dict = dict();
        for word in words1:
            if word in words1Dict:
                words1Dict[word] += 1
            else:
                words1Dict[word] = 1
        words2Dict = dict();
        for word in words2:
            if word in words2Dict:
                words2Dict[word] += 1
            else:
                words2Dict[word] = 1
        
        for word in words1Dict:
            if words1Dict[word] == 1 and word in words2Dict and words2Dict[word] == 1:
                result += 1
        return result