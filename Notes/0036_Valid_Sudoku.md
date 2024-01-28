# 0036. Valid Sudoku

- tag: Array, 2D Array, HashTable
- URL: https://leetcode.com/problems/valid-sudoku/


## Code1

```python
class Solution:
    def isValidSudoku_v1(self, board: List[List[str]]) -> bool:

        r, c = len(board), len(board[0])    # rows, columns
        # freq = dict(int)    
        # Check row
        for i in range(r):
            freq = defaultdict(int)           #(k,v) = (1~9, # of freq) 
            for j in range(c):
                if board[i][j] == ".":
                    continue
                if board[i][j] in freq:
                    return False
                else:
                    freq[board[i][j]] += 1

        # Check col
        for j in range(c):
            freq = defaultdict(int)           #(k,v) = (1~9, # of freq) 
            for i in range(r):
                if board[i][j] == ".":
                    continue
                if board[i][j] in freq:
                    return False
                else:
                    freq[board[i][j]] += 1
        
        # Check sub-box, give key no. for each sub-block
        # key = 3 * (i // 3) +  (j // 3)
        # [0, 1, 2
        #  3, 4, 5,
        #  6, 7, 8]
        freq3 = defaultdict(set)    # (k,v) = (sub-block, set of 1~9)
        for i in range(r):
            for j in range(c):
                key = 3 * (i // 3) +  (j // 3)   # key for 9 sub-blocks
                print("i={}, j={}, key={}".format(i, j, key))
                if board[i][j] == ".":
                    continue
                # Already in the set of sub-blocks that mapped by key
                if board[i][j] in freq3[key]:  
                    return False
                else:
                    freq3[key].add(board[i][j])    # add into the set
        
        return True
        # Time= O(9^2), Space = O(1 + 1 + 9 hashs) for hash
```

```python
[
[".",".",".",".","5",".",".","1","."],
[".","4",".","3",".",".",".",".","."],
[".",".",".",".",".","3",".",".","1"],

["8",".",".",".",".",".",".","2","."],
[".",".","2",".","7",".",".",".","."],
[".","1","5",".",".",".",".",".","."],

[".",".",".",".",".","2",".",".","."],
[".","2",".","9",".",".",".",".","."],
[".",".","4",".",".",".",".",".","."]]
Expect = false
```


### Complexity

- Time:  O(9^2)
- Space: O(1 + 1 + 9 hashs)



## Code2



```python
# Optimized, combined in the same for loop 
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        r, c = len(board), len(board[0])    # rows, columns
        # use 3 dictionary of set: (k,v)= (row no. or col no., set of 1~9)
        freqR = defaultdict(set) # check each row: 
        freqC = defaultdict(set) # check each column
        freqS = defaultdict(set) # check each sub-block

        for i in range(r):
            for j in range(c):
                # no need to check
                if board[i][j] == ".":
                    continue

                key = (i // 3, j // 3) # use tuple to represent sub-block                
                if ( board[i][j] in freqR[i] or
                     board[i][j] in freqC[j] or
                     board[i][j] in freqS[key]):
                     return False

                # Add the seen no. into sets
                freqR[i].add(board[i][j])
                freqC[j].add(board[i][j])
                freqS[key].add(board[i][j])
        
        return True
        # Time= O(9^2), Space = O(9 + 9 + 9 hashs)
```



### Complexity

- Time:  O(9^2)
- Space: O(9 + 9 + 9 hashs)