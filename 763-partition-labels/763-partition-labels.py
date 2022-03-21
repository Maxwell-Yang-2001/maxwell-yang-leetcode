class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        occur = dict()
        for i, c in enumerate(s):
            if c in occur:
                occur[c] = (occur[c][0], i)
            else:
                occur[c] = (i, i)
        
        # they would already be sorted based on dict order based on insertion
        ranges = list(occur.values())
        
        merged_ranges = []
        curr_range = ranges[0]
        
        # merge ranges
        for r in ranges:
            if r[0] > curr_range[1]:
                merged_ranges.append(curr_range)
                curr_range = r
            elif r[1] > curr_range[1]:
                curr_range = (curr_range[0], r[1])
        
        merged_ranges.append(curr_range)
        
        result = []
        
        prev_split = -1
        for r in merged_ranges:
            for i in range(prev_split + 1, r[0]):
                result.append(1)
            result.append(r[1] - prev_split)
            prev_split = r[1]
        
        return result
                
        