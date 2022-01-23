# 135. Candy
# Yuan-Peng Yu
# 01/22/2022

class Solution:
    def candy(self, ratings: List[int]) -> int:
        # No sorting because candies are related to their neighbors (positions).
        # Higher rating children get more candies only than their neighbors, 
        # not lower rating children.  
        
        n = len(ratings)
        candies = [1] * n 
        
        # Pass1  l==>r, make sure candy[right] > candy[left]  
        # left rating < right rating, candy[right] = candy[left] + 1
        for i in range(n-1):
            if ratings[i] < ratings[i+1]:
                candies[i+1] = candies[i] +1
            # print(candies)

        # Pass2 l<==r, make sure candy[left] > candy[right]  
        # left rating > right rating, 
        # update candy[left] = candy[right] + 1
        
        # print("pass2")
        for i in range(n-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                candies[i-1] = max(candies[i-1], candies[i] + 1) 
                # only need to higer than right, but not less than the original
            # print(candies)
        
        return sum(candies)
    # Runtime: 244 ms, faster than 35.28% of Python3
    # Time: O(3n), Space: O(n)
            
            
            
        
        
        