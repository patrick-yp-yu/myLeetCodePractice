# 0040. Combination Sum II

- tag: `Backtracking`
- URL: https://leetcode.com/problems/combination-sum-ii/description/

## Thinking

1. **0039. Combination Sum**
    1. Each number in `candidates` can be used **unlimited number of times**.
2. 0040. Each number in `candidates` may only be used **once** in the combination.
    1. Also, in 0040, the candidates contain duplicate elements.

<br>

## Code1

- the main difference vs **0039. Combination Sum**
    - At the same depth of the tree, only pick unique element once.
    - The given candidates contain duplicates.  `candidates = [10,1,2,7,6,1,5], target = 8`
        - When 1st “1” is picked, the 2nd “1” can be picked at the next depth (next recursion).
        - However, we can not pick “1” again at the same level of the tree (in the same for loop).
    
    
    ```python
        # when in the same height of the tree, each number can only be used once.
        if i > start and candidates[i] == candidates[i-1]:
            continue
    ```
    
- Pruning:
    - `if target - candidates[i] < 0:`
        - we can return directly because of  candidates.sort(). There’s no need to traverse next element

```python
class Solution:        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        self.depth = 0
        result = []                                      
        path = []

        def backtracking(candidates, target, start):
            # Terminal condition
            if target == 0:
                result.append(path.copy())
            if target < 0:
                return
            
            self.depth += 1
            # prev = -1
            for i in range(start, len(candidates)):
                # when in the same height of the tree, each number can only be used once.
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                print("d={}, i={}, s={}, p={}, tarSum={}".format(self.depth,i, start, path+[candidates[i]], target - candidates[i]))
                # Pruning if candidates.sort()  is performed
                # if [1,1,2,5] already > target(8), no need to find [1,1,2,6], [1,1,2,7], and [1,1,2,10] 
                if target - candidates[i] < 0:
                    print("Tree pruned.")
                    return 
                path.append(candidates[i])  # the no. is picked
                backtracking(candidates, target - candidates[i], i + 1)
                path.pop()                  # the no. is not picked 
                # prev = candidates[i]
            self.depth -= 1
        #######
        candidates.sort()                               # !!!Help prune                
        backtracking(candidates, target, 0)
        return result
```

```python
Input: candidates = [10,1,2,7,6,1,5], target = 8

d=1, i=0, s=0, p=[1], tarSum=7
d=2, i=1, s=1, p=[1, 1], tarSum=6
d=3, i=2, s=2, p=[1, 1, 2], tarSum=4
d=4, i=3, s=3, p=[1, 1, 2, 5], tarSum=-1
Tree pruned.
d=4, i=3, s=2, p=[1, 1, 5], tarSum=1
d=5, i=4, s=4, p=[1, 1, 5, 6], tarSum=-5
Tree pruned.
**d=5, i=4, s=2, p=[1, 1, 6], tarSum=0**
d=6, i=5, s=5, p=[1, 1, 6, 7], tarSum=-7
Tree pruned.
d=6, i=5, s=2, p=[1, 1, 7], tarSum=-1
Tree pruned.
d=6, i=2, s=1, p=[1, 2], tarSum=5
**d=7, i=3, s=3, p=[1, 2, 5], tarSum=0**
d=8, i=4, s=4, p=[1, 2, 5, 6], tarSum=-6
Tree pruned.
d=8, i=4, s=3, p=[1, 2, 6], tarSum=-1
Tree pruned.
d=8, i=3, s=1, p=[1, 5], tarSum=2
d=9, i=4, s=4, p=[1, 5, 6], tarSum=-4
Tree pruned.
d=9, i=4, s=1, p=[1, 6], tarSum=1
d=10, i=5, s=5, p=[1, 6, 7], tarSum=-6
Tree pruned.
**d=10, i=5, s=1, p=[1, 7], tarSum=0**
d=11, i=6, s=6, p=[1, 7, 10], tarSum=-10
Tree pruned.
d=11, i=6, s=1, p=[1, 10], tarSum=-3
Tree pruned.
d=11, i=2, s=0, p=[2], tarSum=6
d=12, i=3, s=3, p=[2, 5], tarSum=1
d=13, i=4, s=4, p=[2, 5, 6], tarSum=-5
Tree pruned.
**d=13, i=4, s=3, p=[2, 6], tarSum=0**
d=14, i=5, s=5, p=[2, 6, 7], tarSum=-7
Tree pruned.
d=14, i=5, s=3, p=[2, 7], tarSum=-1
Tree pruned.
d=14, i=3, s=0, p=[5], tarSum=3
d=15, i=4, s=4, p=[5, 6], tarSum=-3
Tree pruned.
d=15, i=4, s=0, p=[6], tarSum=2
d=16, i=5, s=5, p=[6, 7], tarSum=-5
Tree pruned.
d=16, i=5, s=0, p=[7], tarSum=1
d=17, i=6, s=6, p=[7, 10], tarSum=-9
Tree pruned.
d=17, i=6, s=0, p=[10], tarSum=-2
Tree pruned.
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
    - the longest path of recursive tree = the maximal depth of the =

### Reference:

- [https://gitee.com/programmercarl/leetcode-master/blob/master/problems/0040.组合总和II.md](https://gitee.com/programmercarl/leetcode-master/blob/master/problems/0040.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8CII.md)

