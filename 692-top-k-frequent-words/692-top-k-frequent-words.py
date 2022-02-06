class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq_index_dict = dict()
        freq_list = []
        
        # tuple: (frequency, hash, string)
        for word in words:
            if word in freq_index_dict:
                prev_tup = freq_list[freq_index_dict[word]]
                freq_list[freq_index_dict[word]] = (prev_tup[0] - 1, prev_tup[1])
            else:
                freq_index_dict[word] = len(freq_list)
                freq_list.append((-1, word))
            
        freq_list.sort()
        
        result = [''] * k
        for i in range(k):
            result[i] = freq_list[i][1]
        
        return result