class Solution:
    def candy(self, ratings: List[int]) -> int:
        # insert head and tail dummy children for minima
        ratings.append(ratings[-1])
        ratings.insert(0, ratings[0])
        l_ratings = len(ratings)
        candies = [0] * l_ratings
        
        # all children with no higher rating neighbors get 1 candy
        for i, r in enumerate(ratings):
            if (i > 0 and r > ratings[i - 1]) or (i < (l_ratings - 1) and r > ratings[i + 1]):
                continue
            candies[i] = 1
            
        candies[0] = 1
        candies[-1] = 1
        
        prev_min_i = 0
        curr_min_i = 1
        
        while True:
        
            while curr_min_i < l_ratings and candies[curr_min_i] != 1:
                curr_min_i += 1
            
            if curr_min_i == l_ratings:
                break
                
            # gove candies to children between 2 minimas
            for i in range(prev_min_i + 1, curr_min_i):
                if ratings[i] > ratings[i-1]:
                    candies[i] = candies[i-1] + 1
                else:
                    break
            
            for i in range(curr_min_i - 1, prev_min_i, -1):
                if ratings[i] > ratings[i+1]:
                    candies[i] = max(candies[i+1] + 1, candies[i])
                else:
                    break
            
            prev_min_i = curr_min_i
            curr_min_i += 1
        
        # all candies except the head and tail dummy children
        return sum(candies) - 2
        
        
        
            
        