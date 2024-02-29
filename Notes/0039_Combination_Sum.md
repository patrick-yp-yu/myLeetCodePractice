# 0039. Combination Sum

- tag: 'Backtracking'
- URL: https://leetcode.com/problems/combination-sum/description/

## Related questions:

[0216. Combination Sum III](https://leetcode.com/problems/combination-sum-iii)

- In 0216, each number can only be used **once**.
    - Valid number range: 1~9. Traverse the limited range by controlling index.
- In 0039, each number can be used **unlimited number of times.**
    - need to traverse all candidates[i]

## Reference
[programmercarl/leetcode-master（代码随想录出品）](https://gitee.com/programmercarl/leetcode-master/blob/master/problems/0039.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8C.md)

**Backtracking 3 steps**

- Step1, find the **Function Arguments** of the recursive function
- Step2, find the terminal condition (Base case)
- Step3, logic to search the candidates horizontally (in the same depth of the tree)

<br>

## Code1

**Function Arguments** 

- backtracking(candidates, target, currentSum=0, startIndex=0)
    - the last zero is for the index of candidates, not a valid number.
        - vs 0216, start from 1, because it pick a valid number from 1~9.

**Terminal condition (Base case)**

- Terminal condition: when `currSum = targetSum`
    - if `curr > target:` , greater than targetSum, can be pruned.

**Search candidates**

- need to traverse all candidates, start from index: 0~ len(candidates)

```python
class Solution:
    def combinationSum1(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []                                      
        path = []
        self.depth = 0

        def backtracking(candidates, target, curr, start):
            # Terminal condition
            print("{} sum={}".format(path, curr))

            
            if curr > target:   return
            elif curr == target:
                result.append(list(path))               
            
            for i in range(start, len(candidates)):     #
                curr += candidates[i]
                path.append(candidates[i])
                backtracking(candidates, target, curr, i)
                curr -= candidates[i]                   # backtrack
                path.pop()                              # backtrack
        #######

        backtracking(candidates, target, 0, 0)
        return result
```

### Code1 + Pruning:

- Because **candidates[] is already sorted,**
    - `if curr + candidates[i] > target:`
        - we can skip all the candidates that are after `candidates[i]`, because the sum will must be greater than target, return directly.

```python
# Code1 + pruning
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []                                      
        path = []
        self.depth = 0

        def backtracking(candidates, target, curr, start):
            # Terminal condition
            if curr > target:   return
            elif curr == target:
                result.append(list(path))               
            
            for i in range(start, len(candidates)):     #
                # # !!! pruning. When currSum start to > targetSum, no need to execute the for loop
                # because candidates[] is sorted.    
                if curr + candidates[i] > target:                      
                    return                              # because candidates are sorted                
                curr += candidates[i]
                path.append(candidates[i])
                backtracking(candidates, target, curr, i)
                curr -= candidates[i]                   # backtrack
                path.pop()                              # backtrack
        #######
        
        candidates.sort()                               # !!!Help prune
        backtracking(candidates, target, 0, 0)
        return result
```

<br>


### Code4 reduce parameters

**Function Arguments** 

- no need to pass `targetSum` & `candidates[]`
- backtracking(`startIndex=0, curSum=0`)
- the last line: `backtracking(i + 1, curSum)` , increase i to go to next candidates
    - the same function as the for loop in Code1

```python
# Code 4
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        path = []
        
        def backtracking(i, curSum):
            # Base case + pruning
            if curSum == target:
                result.append(path[:])      
                return
            if i >= len(candidates) or curSum > target:              
                return
            
            if curSum + candidates[i] > target:      # pruning
                return 
            # pick the candidate            
            path.append(candidates[i])
            backtracking(i, curSum + candidates[i])
            
            # Not pick the candidate
            path.pop()

            backtracking(i + 1, curSum)              # i+1 = move to next candidate 
        
        #####
        candidates.sort()                           # required
        backtracking(0, 0)
        return result
```

<br>

## Code2 DFS

- When add a number, the `targetSum = targetSum - num`
- Base case: check if `target == 0`

```python
# DFS1
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(candidates, target, path, result):
            
            if target < 0: return       # backtrack
            if target == 0:
                result.append(path[:])
                return
            
            for i, num in enumerate(candidates):
                path.append(num)
                dfs(candidates[i:], target - num, path, result)
                path.pop()
        #######
        result = []
        dfs(candidates, target, [], result)
        return result
```

## Code3 FineTuned Code2

- When passing
- Add self.depth to observe the content of path

```python
# DFS2
    def combinationSum3(self, candidates: List[int], target: int) -> List[List[int]]:
        
        self.depth = 0
        def dfs(candidates, target, path, result):
            
            if target < 0: return       # backtrack
            if target == 0:
                result.append(path)
                return
            self.depth += 1
            for i, num in enumerate(candidates):
                print("d={}, p={}, tarSum={}".format(self.depth, path+[num], target - num))             
                dfs(candidates[i:], target - num, path+[num], result)
            
            self.depth -= 1
        #######
        result = []
        dfs(candidates, target, [], result)
        return result
```

```python
Input: candidates = [2,3,6,7], target = 7

d=1, p=[2], tarSum=5
d=2, p=[2, 2], tarSum=3
d=3, p=[2, 2, 2], tarSum=1
d=4, p=[2, 2, 2, 2], tarSum=-1
d=4, p=[2, 2, 2, 3], tarSum=-2
d=4, p=[2, 2, 2, 6], tarSum=-5
d=4, p=[2, 2, 2, 7], tarSum=-6
d=3, p=[2, 2, 3], tarSum=0
d=3, p=[2, 2, 6], tarSum=-3
d=3, p=[2, 2, 7], tarSum=-4
d=2, p=[2, 3], tarSum=2
d=3, p=[2, 3, 3], tarSum=-1
d=3, p=[2, 3, 6], tarSum=-4
d=3, p=[2, 3, 7], tarSum=-5
d=2, p=[2, 6], tarSum=-1
d=2, p=[2, 7], tarSum=-2
d=1, p=[3], tarSum=4
d=2, p=[3, 3], tarSum=1
d=3, p=[3, 3, 3], tarSum=-2
d=3, p=[3, 3, 6], tarSum=-5
d=3, p=[3, 3, 7], tarSum=-6
d=2, p=[3, 6], tarSum=-2
d=2, p=[3, 7], tarSum=-3
d=1, p=[6], tarSum=1
d=2, p=[6, 6], tarSum=-5
d=2, p=[6, 7], tarSum=-6
d=1, p=[7], tarSum=0
final output=[[2, 2, 3], [7]]
```

### Complexity

- Time:  $O(n^{\frac{T}{M}+ 1})$
    - This would be an upper bound.
    - The backtracking is a DFS traversal in n-ary tree. Time is decided by the traversed notes in the tree. ⇒ $O(n^{treeDepth})$
    - In the worst case, each time pick the minimal number. So, reaching targetSum will need more recursion (more depth).
        - T = target value
        - M = min(candidates[array])
        - the maximal depth of the = $\frac{T}{M}$
        - the maximal number of node in the tree = $N^{\frac{T}{M}+1}$
- Space: = $O(\frac{T}{M})$
    - the longest path of recursive tree = the maximal depth of the = $\frac{T}{M}$
