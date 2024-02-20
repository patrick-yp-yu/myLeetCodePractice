# 0077. Combinations

- tag: `Backtracking`
- URL: https://leetcode.com/problems/combinations/

# Related questions:

- [0216. Combination Sum III](https://leetcode.com/problems/combination-sum-iii)


# Code1


```python
def combine(self, n: int, k: int) -> List[List[int]]:
        
        result = []
        path   = []
        
        def backtracking(n, k, start):
            
            # Terminal condition
            if len(path) == k: # k-number combination
                result.append(list(path)) # !!!
                # print("res=", result)
                return
            
            for i in range(start, n+1):
                path.append(i)                          # process current node
                backtracking(n, k, i + 1)               # recursive
                path.pop()                              # backtrack
                
        ########

        backtracking(n, k, 1)  # combinations start from 1
        return  result
```

### Complexity

- Time: because tree height = k, 1st level has n branches, time complexity upper bound = n^k
    - leecode solution = $O(kC^k_N)$

### Reference:

- [https://gitee.com/programmercarl/leetcode-master/blob/master/problems/0077.组合.md](https://gitee.com/programmercarl/leetcode-master/blob/master/problems/0077.%E7%BB%84%E5%90%88.md)

<br>

# Code2 With pruning
- A valid path need to contain k number
    - In the for loop, if the number from `startIndex` to end is not enough k. Don’t need to continue. Can prune.
```python
###
    # With pruning
    # Picked number= path.size()
    # Total need k number, still need = k - path.size() number 
    # Upper bound n - the number still need (k-path.size) + 1 to become index
    # range=[startIndex, n] => the range are included
    # pruning = [startIndex, n - (k - path.size()) +1]
    #         = [startIndex, n - (k - path.size()) +1 +1 ) become [,)
    def combine2(self, n: int, k: int) -> List[List[int]]:
        result = []
        path   = []
        
        def backtracking(n, k, start):
            
            # Terminal condition
            if len(path) == k: # k-number combination
                result.append(list(path)) # !!!
                # print("res=", result)
                return
            
            for i in range(start, n- (k-len(path)) +2): # With pruning!!!
                path.append(i)                          # process current node
                backtracking(n, k, i + 1) # recursive
                path.pop()                              # backtrack
                
        ########

        backtracking(n, k, 1)
        return  result
```
### Complexity

- Time: O(n* 2^n)
    - horizontal, for loop: O(n)
    - vertical, recursive tree: O(2^n)
- Space: O(n)

### Reference:

- [https://gitee.com/programmercarl/leetcode-master/blob/master/problems/0077.组合优化.md](https://gitee.com/programmercarl/leetcode-master/blob/master/problems/0077.%E7%BB%84%E5%90%88%E4%BC%98%E5%8C%96.md)
