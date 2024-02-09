# 2104. Sum of Subarray Ranges

- tag: MonotonicStack
- URL: https://leetcode.com/problems/sum-of-subarray-ranges/description/


## Code1 Brute Force

- For each subarray, find the max number & the min number

```python
class Solution:
    # Brute force: find cur_max, cur_min when traversing subarray
    def subArrayRanges_1(self, nums: List[int]) -> int:
        
        n = len(nums)
        range_sum = 0 

        for i in range(n):
            # reset min, max for each i
            cur_max, cur_min = float('-inf'), float('inf') 
            for j in range(i, n):
                cur_max = max(cur_max, nums[j])
                cur_min = min(cur_min, nums[j])
                range_sum += cur_max - cur_min

        return range_sum
    #  Time: O(n^2), Space: O(1)
```

### Complexity

- Time: O(n^2)
- Space: O(1)

<br>

## Code2  Monotonic Stack

- Use the same method in  [0907. Sum of Subarray Minimums](https://www.notion.so/0907-Sum-of-Subarray-Minimums-0a38869d80e24eeba6728e8ad5b3d05d?pvs=21)
    - Find the contribution of the minimum number in each subarray
- $\sum range = \sum (maxValue - minValue) = \sum maxValue - \sum minValue$

```python
# Sol2: Monotonic Stack 
    # Refer to 0907_Sum_of_Subarray_Minimums
    def subArrayRanges(self, nums: List[int]) -> int:

        nums_min = [float('-inf')] + nums + [float('-inf')]
        nums_max = [float('inf')] + nums + [float('inf')] 
        min_stk = []
        max_stk = []
        sum_min = 0
        sum_max = 0

        # Find the sum of (the minimum for each subarray)
        for i, num in enumerate(nums_min):
            while min_stk and num < nums_min[min_stk[-1]]:
                min_idx = min_stk.pop()
                l_bound = min_stk[-1] if min_stk else -1    
                r_bound = i

                counts = (min_idx - l_bound) * (r_bound - min_idx) 
                sum_min += nums_min[min_idx] * counts
            min_stk.append(i)

        # Find the sum of (the maximum for each subarray)
        for i, num in enumerate(nums_max):
            while max_stk and num > nums_max[max_stk[-1]]:
                max_idx = max_stk.pop()
                l_bound = max_stk[-1] if max_stk else -1    
                r_bound = i

                counts = (max_idx - l_bound) * (r_bound - max_idx) 
                sum_max += nums_max[max_idx] * counts
            max_stk.append(i)
        
        return sum_max - sum_min
     #  Time: O(n), Space: O(n) because of stack
```

### Complexity

- Time: O(n)
- Space: O(n)