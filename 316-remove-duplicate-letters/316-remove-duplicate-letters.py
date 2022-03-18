class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq = dict()
        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        
        letters = list(freq)
        letters.sort()
        
        result = []
        
        prev_i = 0
        i = 0
        while letters:
            print(i)
            print(freq)
            print(letters)
            fullfilled = False;
            while True:
                if s[i] in freq:
                    freq[s[i]] -= 1
                # best case: smallest letter
                if s[i] == letters[0]:
                    fullfilled = True
                    break
                if s[i] in freq and freq[s[i]] == 0:
                    break
                i += 1
            
            # if fullfilled, could continue onwards
            if fullfilled:
                result.append(s[i])
                del freq[s[i]]
                letters.remove(s[i])
                prev_i = i = i + 1
                continue
            
            # otherwise, look back to find smallest letter
            smallest_index = i
            for curr in range(prev_i, i + 1):
                if s[curr] in freq and (s[curr] < s[smallest_index] or (s[curr] == s[smallest_index] and curr < smallest_index)):
                    smallest_index = curr
            
            result.append(s[smallest_index])
            del freq[s[smallest_index]]
            
            # add back frequencies
            for curr in range(smallest_index + 1, i + 1):
                if s[curr] in freq:
                    freq[s[curr]] += 1
            
            prev_i = i = smallest_index + 1
            letters.remove(s[smallest_index])
        
        return ''.join(result)    
        