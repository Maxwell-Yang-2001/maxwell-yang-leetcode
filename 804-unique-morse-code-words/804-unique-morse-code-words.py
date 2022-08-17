class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_map = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        morses = set()
        ord_a = ord('a')
        
        for w in words:
            morse = ''
            for c in w:
                morse += morse_map[ord(c) - ord_a]
            morses.add(morse)
        
        return len(morses)
                