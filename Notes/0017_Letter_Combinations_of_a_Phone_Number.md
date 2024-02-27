# 0017. Letter Combinations of a Phone Number

tag: Backtracking
URL: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# Thinking

1. Backtracking, combination type problem
2. For each number, candidates = the letters under the phone number 
    1. Need to create a mapping from number to letters
    
    ```
            mapping  = {"2": "abc",
                        "3": "def",
                        "4": "ghi",
                        "5": "jkl",
                        "6": "mno",
                        "7": "pqrs",
                        "8": "tuv", 
                        "9": "wxyz"}
    ```
    
3. `digits = "23"`
    1. 2: “abc”; 3: “def” 
    2. total combinations = 3 choice * 3 choice = 9
4. Backtracking trees:
    
    ![Screenshot 2024-02-26 at 9.05.29 PM.png](0017%20Letter%20Combinations%20of%20a%20Phone%20Number%201cacf8acbf2149a78f5d89e968eac7ec/Screenshot_2024-02-26_at_9.05.29_PM.png)
    
- for each node, there are at most 4  choices (because of worst cases: `"7": "pqrs”`, `"9": "wxyz"`)
- len(digits) = n = tree depth
- total combinations = 4^n
- To add together need O(n)
- ⇒ total time complexity = $O(n * 4^n)$

# Code1

- base case = reach the leaf node,
    - result.append( chosen candidates in the path)
- Choose candidates (traverse different letters)

```python
class Solution:
    #
    def letterCombinations(self, digits: str) -> List[str]:
        # mapping numbers to letters 
        mapping  = {"2": "abc",
                    "3": "def",
                    "4": "ghi",
                    "5": "jkl",
                    "6": "mno",
                    "7": "pqrs",
                    "8": "tuv", 
                    "9": "wxyz"}
        result = []
        self.path = ""      # path = string type in this question
                            #sequential nodes: 2~9 from top-dowm
        
        def backtracking(idx):
            
            # base case: (reach the leaf node)
            if idx == len(digits):   # traversed all decision selecting already
                result.append(self.path)
                return
            
            letters = mapping[digits[idx]]
            for ch in letters:
                self.path = self.path + ch          # try next candidate 
                backtracking(idx + 1)               # explore the candidate
                self.path = self.path[0:-1]         # Revemoe the candidate. Not include the last character
                
                
        #####
        if len(digits) == 0: return []
        backtracking(0)
        return result
```

### Reference:

- [https://www.youtube.com/watch?v=0snEunUacZY&list=PLot-Xpze53lf5C3HSjCnyFghlW0G1HHXo&index=7&ab_channel=NeetCode](https://www.youtube.com/watch?v=0snEunUacZY&list=PLot-Xpze53lf5C3HSjCnyFghlW0G1HHXo&index=7&ab_channel=NeetCode)

### Complexity

- Time: $O(n * 4^n)$
- Space: O(n),

# Code2

- 

```python

```

### Reference:

- 

### Complexity

- Time:
- Space: