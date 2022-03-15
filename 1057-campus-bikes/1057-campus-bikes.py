class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        lw, lb = len(workers), len(bikes)
        # distance is in range [0, 1998]
        worker_list = [-1] * lw
        bike_list = [-1] * lb
        
        distance_dict = [[] for i in range(2000)]
        
        for wi, w in enumerate(workers):
            for bi, b in enumerate(bikes):
                distance = abs(w[0] - b[0]) + abs(w[1] - b[1])
                distance_dict[distance].append((wi, bi))
        
        counter = 0
        for distance_group in distance_dict:
            distance_group.sort()
            for pair in distance_group:
                # if either worker or bike has been assigned, skip it
                if worker_list[pair[0]] >= 0 or bike_list[pair[1]] >= 0:
                    continue
                worker_list[pair[0]] = pair[1]
                bike_list[pair[1]] = pair[0]
                counter += 1
                if counter == lw:
                    break
            if counter == lw:
                break
        
        return worker_list