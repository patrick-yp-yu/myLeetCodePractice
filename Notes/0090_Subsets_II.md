# 0090. Subsets II

- tag: `Backtracking`
- URL: https://leetcode.com/problems/subsets-ii/description/

## Related questions

- [0078. Subsets](https://leetcode.com/problems/subsets/)

<br>


# [0090. Subsets II](https://leetcode.com/problems/subsets-ii)

1. nums array only contains unique elements


- **0090.** contain duplicated elements

- total number of subset = $2^n$, each subset length can up to n
    - total time complexity = $O(n \cdot 2^n)$
- Need to `nums.sort()` in the begining.
    
    ![0090_Subsets_II.png](/Notes/images/0090_Subsets_II.png)
    
- Two decision tree branches:
    - include `nums[i]`
    - NOT include `nums[i]`
        - if `nums[i]` has duplicates, **jump index until no duplicates.**
    

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def backtrack(i):
            # Base case
            if i >= len(nums):      # visited all nodes
                result.append(subset[:])
                return 

            # Recursive case
            # 1. All subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1)

            # 2. All subsets that NOT include nums[i]
            subset.pop()    # not include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i+1]:   # in-bound & duplicated candidate
                i += 1                                          # [1,2,2,3] i=1 => i= 2 => i +1 = 3
            backtrack(i + 1)
        ####
        nums.sort()
        backtrack(0)
        return result
```

### Complexity

- Time: $O(n \cdot 2^n)$
- Space: $O(n \cdot 2^n)$