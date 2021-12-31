class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if sentence.find(c) == -1:
                return False
        return True