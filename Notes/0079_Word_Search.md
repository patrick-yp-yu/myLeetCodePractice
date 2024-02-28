# 0079. Word Search

- tag: `Backtracking`
- URL: https://leetcode.com/problems/word-search/

<br>

# **Backtracking Template**

[https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/2793/](https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/2793/)

```python
def backtrack(candidate):
		# Base case:
    if find_solution(candidate):
        output(candidate)
        return
    
		# Recursive case:
    # iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):   # 需不需要 explore, 可不可以剪枝
            # try this partial candidate solution
            place(next_candidate)

            # given the candidate, explore further.
            backtrack(next_candidate)

            # backtrack
            remove(next_candidate)
```

- Unlike brute-force search, in backtracking algorithms we are often able to determine if a partial solution candidate is worth exploring further (*i.e.* `is_valid(next_candidate)`), which allows us to prune the search zones. This is also known as the constraint, *e.g.* the attacking zone of queen in N-queen game.

<br>


# Code1

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            
            if i == len(word):              # visited all chars in the word 
                return True 
            
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS):
                return False
            
            if word[i] != board[r][c]:      # character not match. Char match => continue 
                return False    

            if (r, c) in path:              # The same cell may not be used more than once.
                return False
            
            path.add((r,c))

            # Check 4 directions
            # result = exist or not exist
            result = (dfs(r - 1, c, i + 1) or
                      dfs(r + 1, c, i + 1) or
                      dfs(r, c - 1, i + 1) or
                      dfs(r, c + 1, i + 1))
            path.remove((r,c))
            return result

        ##########
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):    # return True when match all chars in word 
                    return True

        # Else 
        return False
```

### Reference:

- [https://www.youtube.com/watch?v=pfiQ_PS1g8E](https://www.youtube.com/watch?v=pfiQ_PS1g8E)

### Complexity

- Time: O(rows*cols * dfs) = O( r*c * 4^n) = O(n* 4^n)
    - There are n*m grids
    - For each grid, dfs(r,c, i) will be called. The time complexity of dfs = 4^n, because there are 4 directions for each position
- Space: O(n)
