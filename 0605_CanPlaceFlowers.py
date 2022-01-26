# 605. Can Place Flowers
# Yuan-Peng Yu
# 01/25/2022


# Sol1. Find the max #flowers that can be placed, then compare with n 
class Solution:
    
    # Sol1
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        count = 0
        length = len(flowerbed)
        for i, f in enumerate(flowerbed):
            if f == 0: # empty, can place flowers
                # check left neighbor and right neighbor == 0
                if (i == 0 or flowerbed[i-1] == 0) and (i == length-1 or flowerbed[i+1] == 0):
                    flowerbed[i] = 1 # can place flower
                    count += 1
        
        return count >= n
    # Runtime: 164 ms, faster than 87.33% of Python3
    # Time: O(N)
    # Space: O(N)
    

    