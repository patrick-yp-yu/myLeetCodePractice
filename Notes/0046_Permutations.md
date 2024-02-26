# 0046. Permutations

- tag: `Backtracking`
- URL: https://leetcode.com/problems/permutations/

# Related Questions

[47. Permutations II](https://leetcode.com/problems/permutations-ii)

# Thinking

1. The given numbers in the array are distinct. No duplicates. 

<br>

# Code1 Backtracking template

- Add an extra array `used` to record which element is used.

```python
    ### Sol1: Add a used_array to record
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtracking(nums, path, used):
            # Terminal condition
            if len(path) == len(nums):      # picked all numbers
                result.append(list(path))
                return
            
            # select from candidates
            for i in range(len(nums)):
                if used[i]:                 # item is used, go to next
                    continue
                used[i] = True
                path.append(nums[i])            # make choice
                backtracking(nums, path, used)  # recursive
                path.pop()                      # unmake choice
                used[i] = False

        ##
        result = []
        used_arr = [False] * len(nums)
        backtracking(nums, [], used_arr)
        return result
```

### Reference:

- [https://gitee.com/programmercarl/leetcode-master/blob/master/problems/0046.全排列.md](https://gitee.com/programmercarl/leetcode-master/blob/master/problems/0046.%E5%85%A8%E6%8E%92%E5%88%97.md)

<br>

# Code2 Recursive directly the function itself


```python
class Solution:        
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        # base case
        if len(nums) == 1:
            return [nums[:]]    # faster than nums.copy()
        
        for i in range(len(nums)):
            n = nums.pop(0)     # nums pop index 0 
            
            permutations = self.permute(nums)
            print("permu={}, append pop={}".format(permutations, n))
            
            # Append poped node, ex: n=1, [2,3] [3,2] => [2,3,1] [3,2,1]
            for x in permutations:      
                x.append(n) 
            result.extend(permutations)
            
            print("   result={}".format(result))
            nums.append(n)

        return result
```

Running:

- Base case: only left one element = leaf node,
- (returned permutations) append the 1st poped out element

```python
permu=[[3]], append pop=2
   result=[[3, 2]]
permu=[[2]], append pop=3
   result=[[3, 2], [2, 3]]
permu=[[3, 2], [2, 3]], append pop=1
   result=[[3, 2, 1], [2, 3, 1]]
permu=[[1]], append pop=3
   result=[[1, 3]]
permu=[[3]], append pop=1
   result=[[1, 3], [3, 1]]
permu=[[1, 3], [3, 1]], append pop=2
   result=[[3, 2, 1], [2, 3, 1], [1, 3, 2], [3, 1, 2]]
permu=[[2]], append pop=1
   result=[[2, 1]]
permu=[[1]], append pop=2
   result=[[2, 1], [1, 2]]
permu=[[2, 1], [1, 2]], append pop=3
   result=[[3, 2, 1], [2, 3, 1], [1, 3, 2], [3, 1, 2], [2, 1, 3], [1, 2, 3]]
```

### Reference:

- [https://www.youtube.com/watch?v=s7AvT7cGdSo&ab_channel=NeetCode](https://www.youtube.com/watch?v=s7AvT7cGdSo&ab_channel=NeetCode)

<br>

# Code3 using swap

- From leetcode solution:
    - using swap
    

```python
###
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(start):
            
            if start == len(nums):      # Reach leaf node
                result.append(nums[:])
            
            
            for i in range(start, len(nums)):
                
                nums[i], nums[start] = nums[start], nums[i]     # swap
                dfs(start + 1)
                nums[i], nums[start] = nums[start], nums[i]     # swap back
        
        result = []
        dfs(0)
        return result
```

### Reference:

- Leetcode solution 

### Complexity

- Time: time complexity should be `N x N!`.
    - Each path (from root to leaf node) ＝ 1 permutation.  Need N! time complexity， 
    - Then, add all paths into result = O(N) time。⇒ `N x N!`.
    - Initially we have `N` choices, and in each choice we have `(N - 1)` choices, and so on. Notice that at the end when adding the list to the result list, it takes `O(N)`.
- Space: Second, the space complexity should also be `N x N!`
 since we have `N!` solutions and each of them requires `N` space to store elements.

