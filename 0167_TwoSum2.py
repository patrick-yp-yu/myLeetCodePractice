# 0167. Two Sum II - Input Array Is Sorted
# Yuan-Peng Yu
# 01/25/2022

class Solution:
    # Sol1 dictionary
    def twoSum1(self, numbers: List[int], target: int) -> List[int]:
        
        table = defaultdict()
        for i, num in enumerate(numbers):
            table[num] = i+1 # (key, value) = (number, index). The index start with 1
            
        
        for i, num in enumerate(numbers):
            find = target - num
            if find in table:
                return [i+1, table[find]]
    # Runtime: 97 ms, faster than 32.50% of Python3
    # Memory Usage: 14.6 MB, less than 87.19%
    # Time: O(2n) = O(n)
    # Space: O(n) because of dicitionary
    
    ### -------------------------------------
    
    # Sol2 two-pointers
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l, r = 0, len(numbers) - 1
        
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l+1, r+1] # 1-based index
            elif sum < target: # move left
                l += 1
            else:
                r -= 1
                
        return [-1, -1] # if no solutions
    # Runtime: 63 ms, faster than 77.06% of Python3
    # Memory Usage: 14.8 MB, less than 34.53% 
    # Time: O(n) traverse array once
    # Time: O(1) only stores l, r, & sum