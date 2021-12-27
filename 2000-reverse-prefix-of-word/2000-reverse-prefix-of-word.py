class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            index = word.index(ch)
            return ''.join([x for x in word[:index+1]][::-1]) + word[index+1:]
        return word