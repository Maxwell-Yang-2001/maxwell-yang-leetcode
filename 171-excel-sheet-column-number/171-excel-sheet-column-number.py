class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        ord_ref = ord('A') - 1
        for col in columnTitle:
            result = 26 * result + ord(col) - ord_ref
        
        return result