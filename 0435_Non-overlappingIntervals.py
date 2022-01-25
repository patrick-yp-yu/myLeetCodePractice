# 435. Non-overlapping Intervals
# Yuan-Peng Yu
# 01/24/2022


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort() # O(nlog(n))
        nonoverlap = 0
        
        pre_end = -math.inf
        for cur_start, cur_end in intervals:  # O(n)
            if pre_end <= cur_start:  # non-overlapped
                nonoverlap += 1
                pre_end = cur_end # set value
            
            else: # overlapped
                pre_end = min(pre_end, cur_end)
        
        return len(intervals) - nonoverlap
                
    # Runtime: 2234 ms, faster than 24.28% of Python3
    # Time: O(nlog(n)) + O(n) = O(nlog(n))
    # Space: O(n)