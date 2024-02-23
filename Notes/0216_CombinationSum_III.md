# 0216. Combination Sum III

- tag: `Backtracking`
- URL: https://leetcode.com/problems/combination-sum-iii/description/



# Related questions:
- [39. Combination Sum](https://leetcode.com/problems/combination-sum)
- [40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii)
- [377. Combination Sum IV](https://leetcode.com/problems/combination-sum-iv)

<br>

# Backtracking Template

```python
result = []

def is_valid_path(path):
    # check if it is a valid solution
    return True

def backtrack(path, candidates_list):

    if is_valid_path():
        result.add(path.copy())         # Update answer, add instance
        return

    for choice in candidates_list
        path.add(choice)                # make_choice
        backtrack(path, candidates_list)   # recursive
        path.pop(choice)                # unmake_choice

```

<br>

# Code1 Backtracking

- Terminal condition 1: `len(path)== k`,
    - the equals the depth of the tree (picked k numbers)
- Terminal condition 2: `curSum == targetSum`
- candidates_range: 1~9, can only pick integer 1~9
    - Each number is used **at most once**. Decided by `start`
    - this is the width of three

```python
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        result = []
        path   = []
        
        def backtracking(k, targetSum, curSum, start):
            
            # Terminal condition
            if len(path) == k:                          # k-number combination
                if curSum == targetSum:                 # valid condition
                    result.append(list(path))           # !!! a copy that does not change
                    return
            
            for i in range(start, 10):                  # valid range 1~9
                curSum += i
                path.append(i)                          # process current node
                backtracking(k, targetSum, curSum, i + 1) # recursive
                curSum -= i
                path.pop()                              # backtrack
                
        ########

        backtracking(k, n, 0, 1)                        # start from number1, not 0
        return  result
```

### Complexity

- Time: O(n * 2^n)
- Space: O(n)

### Reference:

- [https://gitee.com/programmercarl/leetcode-master/blob/master/problems/0216.组合总和III.md](https://gitee.com/programmercarl/leetcode-master/blob/master/problems/0216.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8CIII.md)