# 0496_nextGreaterElement

from collections import defaultdict 

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        # 1. Use stack, 
        # 2. pop while curr num > stack.top, 
        #    map the poped element to curr num, which is the next greater element 
        # 3. Go through nums1, find the (k,v) 

        table = defaultdict(int)
        stack = []
        for i, x in enumerate(nums2):
            # Pop when found the next greater 
            while len(stack) > 0 and stack[-1] < x: 
                table[ stack.pop() ] = x
            # push
            stack.append(x)     

        ans = []
        for i, x in enumerate(nums1):
            if x in table:
                ans.append(table[x])
            else:
                ans.append(-1)
        return ans


nums1 = [1,2,4,6]
nums2 = [6,2,1,5,4]
## output = [5,5,-1,-1]
# nums1 = [4,1,2]
# nums2 = [1,3,4,2]

sol = Solution()
ans1 = sol.nextGreaterElement(nums1, nums2)
print(ans1)