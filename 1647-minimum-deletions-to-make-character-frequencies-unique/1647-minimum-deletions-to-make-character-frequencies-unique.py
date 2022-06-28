class Solution:
    def minDeletions(self, s: str) -> int:
        freq_dict = collections.defaultdict(lambda: 0)
        for c in s:
            freq_dict[c] += 1
        
        freq_list = list(freq_dict.values())
        freq_list.sort(reverse=True)
        
        prev = freq_list[0] + 1
        
        result = 0
        for freq in freq_list:
            if freq >= prev:
                new_freq = max(0, prev - 1)
                result += (freq - new_freq)
                freq = new_freq
            prev = freq
        return result
                