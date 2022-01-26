# Sol1. Find the max #flowers that can be placed, then compare with n 
class Solution:
    
    # Sol1
    def canPlaceFlowers1(self, flowerbed: List[int], n: int) -> bool:
        
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
    # Memory Usage: 14.5 MB, less than 61.69% of Python3 
    # Time: O(N)
    # Space: O(N)
    ###-----------------------------------------------------
    
    # Sol2. compare previout vs current
    # prev curr
    # 0    0   => can plant
    # 0    1   => cannot plant due to planted already
    # 1    0   => cannot plant due to neighbor
    # 1    1   => previous planted flower need to be removed because curr ==1
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    
        count = 0
        prev = 0
        
        for curr in flowerbed:
            if curr == 0:
                if prev == 0: # 0, 0 => can plant 
                    count += 1
                    curr = 1
                    prev = curr
                else: # prev = 1
                    # cannot plant due to neighbor
                    prev = curr
            
            else: # curr ==1
                if prev == 0:
                    # cannot plant due to planted already
                    prev = 1 # update prev = curr
                else: # prev = 1
                    count -= 1 #previous planted flower need to be removed because curr ==1 
                    prev = 1
        return count >= n
    # Runtime: 173 ms, faster than 72.02% of Python3
    # Memory Usage: 14.4 MB, less than 84.39% of Python3 
    # Time: O(N)  traverse the list
    # Space: O(1), only have fixed variables
    