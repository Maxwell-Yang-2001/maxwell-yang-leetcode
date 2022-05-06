class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        pair_list = []
        curr_char, curr_count = '!', 0
        for c in s:
            if c == curr_char:
                curr_count += 1
            else:
                pair_list.append([curr_char, curr_count])
                curr_char, curr_count = c, 1
        pair_list.pop(0)
        pair_list.append([curr_char, curr_count])
        
        index = 0
        while index < len(pair_list):
            
            if pair_list[index][1] >= k:
                remainder = pair_list[index][1] % k
                if remainder == 0:
                    pair_list.pop(index)
                    # need to merge if necessary
                    if index - 1 >= 0 and index < len(pair_list) and pair_list[index - 1][0] == pair_list[index][0]:
                        pair_list[index - 1][1] += pair_list[index][1]
                        pair_list.pop(index)
                        index -= 1
                else:
                    pair_list[index][1] = remainder
                    index += 1
            else:
                index += 1
        
        result = []
        for pair in pair_list:
            for count in range(pair[1]):
                result.append(pair[0])
        
        return ''.join(result)