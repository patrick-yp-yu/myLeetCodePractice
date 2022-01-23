# 84. Largest Rectangle in Histogram

class Solution:
    ## Brute force with pruning.
    ## Time = O(n^2) => Time Limit Exceeded
    ## Logic
    ## 1. Outer loop: find the highest peak
    ## 2. Inner: find the min limited height toward left  
    # if len(heights) == 1:
    #     return heights[0]    
    def largestRectangleArea1(self, heights):

        max_area = 0
        for i in range(0, len(heights)):
            # Contine to find next larger, until meet the smaller 
            if i+1 < len(heights) and heights[i] <= heights[i+1]: 
                continue    
            h_limit = heights[i]  # the limited height 
            for j in range(i, -1, -1):  # (start, stop, step)
                h_limit = min(h_limit, heights[j])
                area = h_limit * (i-j+1)
                print(f'{i}, {j}, h_limit= {h_limit}, {area} vs {max_area}')     
                max_area = max(max_area, area)
        return max_area
    
    # Monotonic increasing stack 
    # O(n) 
    def largestRectangleArea(self, heights):

        # heights.insert(0, 0) 
        heights.append(0)
        max_area = 0
        stack = [-1]    # (index, retangle height)
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]  
                idx = stack[-1]
                width = i - idx -1
                # print(f'{i}, idx={idx}, area= {height}*{width}; vs {max_area}')     
                max_area = max(max_area, height * width) 
            stack.append(i)
            # print(f'{i}, stk={stack}')
        
        # print('------------------')
        return max_area                

import unittest 
class TestResult(unittest.TestCase):
    def test_1(self):
        result1 = Solution().largestRectangleArea([2,1,5,6,2,3])
        expect1 = 10
        self.assertEqual(result1, expect1)
    
    def test_2(self):
        result2 = Solution().largestRectangleArea([2,4])
        expect2 = 4
        self.assertEqual(result2, expect2)

    def test_3(self):
        result = Solution().largestRectangleArea([2,1,2])
        expect = 3
        self.assertEqual(result, expect)

# unittest.main()

h1 = [2,1,2]
ans1 = Solution()
print(ans1.largestRectangleArea(h1))



