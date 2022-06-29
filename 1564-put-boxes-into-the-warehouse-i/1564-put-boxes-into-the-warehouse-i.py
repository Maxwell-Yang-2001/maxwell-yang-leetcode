class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        warelist = []
        min_height = warehouse[0]
        curr_count = 0
        for height in warehouse:
            if height >= min_height:
                curr_count += 1
            else:
                warelist.append((min_height, curr_count))
                min_height = height
                curr_count = 1
        warelist.append((min_height, curr_count))
        warelist.reverse()
        
        boxes.sort()
        slot_index = 0
        curr_height, curr_count = warelist[slot_index]
        l_ware = len(warelist)
        result = 0
        for b in boxes:
            while b > curr_height:
                slot_index += 1
                if slot_index == l_ware:
                    return result
                curr_height, curr_count = warelist[slot_index]
            result += 1
            curr_count -= 1
            if curr_count == 0:
                slot_index += 1
                if slot_index == l_ware:
                    return result
                curr_height, curr_count = warelist[slot_index]
        
        return result
                