# 0856. Score of Parentheses

- tag: `MonotonicStack`
- URL: https://leetcode.com/problems/score-of-parentheses/

## Thinking

1.  `()` = 1 for  the depth = 0. This is the special case.
2.  `(A)` =  2*A,  for  any depth > 0


## Code1

- push a default depth (0) into the stack
- the depth will affect the score for a closed ()
    - the depth is actually the score when closed a ()
    - if depth == 0:  score += 1
    - if depth > 0: score += 2* depth
    - `AB` has score `A + B`, this is completed by `stack[-1] +=  a score when closed ()`

```python
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0] # record depth of parentheses
        depth = 0   # default depth, depth = affect score for a closed ()
        
        for x in s:
            if x == '(':    # Open (
                stack.append(0)
                # print(f"(: {stack}")

            else:           # Close )
                depth = stack.pop()
                if depth == 0:
                    stack[-1] += 1
                else:
                    stack[-1] += 2 * depth
                # print(f"): {stack}, depth={depth}")

        return stack[-1]
```

```python
s ="()"

(: [0, 0]
): [1], depth=0

#################
s ="(())"
(: [0, 0]
(: [0, 0, 0]
): [0, 1], depth=0
): [2], depth=1

#################
s ="()()"
(: [0, 0]
): [1], depth=0
(: [1, 0]
): [2], depth=0

#################
s ="(()(()))"

(: [0, 0]
(: [0, 0, 0]
): [0, 1], depth=0
(: [0, 1, 0]
(: [0, 1, 0, 0]
): [0, 1, 1], depth=0
): [0, 3], depth=1
): [6], depth=3
```

### Similar way

- use `max()`  to simplify if-else
    - when v = 0, depth = 0: score += 1
    - when v ≥ 1, depth ≥ 1: score += 2* depth

```python
class Solution(object):
    def scoreOfParentheses(self, S):
        stack = [0] #The score of the current frame

        for x in S:
            if x == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)

        return stack.pop()
```

### Complexity

- Time: O(n)
- Space: O(n)

