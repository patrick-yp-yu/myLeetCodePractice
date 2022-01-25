# 452. Minimum Number of Arrows to Burst Balloons
# Yuan-Peng Yu
# 01/25/2022

# Greedy Algorithm
# Similar to the "intervals scheduling". Think ballons as intervals.
# 1. Interval scheduling finds the max # of non-overlapped intervals
# 2. This question find the min # of arrows
# if intervals are non-overlapped, need 1 more arrow

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort(key = (lambda x:x[1])) # sort by end value

        num_arrows = 0 
        
        pre_end = -math.inf
        for cur_start, cur_end in points:
            if cur_start > pre_end: # there is no overlap, need 1 more arrow
                num_arrows += 1
                pre_end = cur_end # set new end 
        
        return num_arrows
    # Runtime: 1367 ms, faster than 77.79% of Python3
    # Time: O(NlogN) + O(N) = O(NlogN)
    # Space: O(N)