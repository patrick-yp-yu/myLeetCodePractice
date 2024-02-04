# 0155. Min Stack

- tag: Stack
- URL: https://leetcode.com/problems/min-stack/description/

## Thinking

1. The question requires O(1), 
    - `Binary Search Tree` or `Heap` need O(logn)，cannot use them. 
    -  Use space to exchange time, add an extra list as a stack to record the min. value



## Code1

- when we push a  new element, we compare the value immediately with the top element in the min-stack.
    - At push(), the min-stack is pushed a value, which is the min. value.
    - so, the top element in the min-stack = min value every time

```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.minstk = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        # Compare min
        if len(self.minstk) != 0:
            val = min(val, self.minstk[-1])
        self.minstk.append(val)

    def pop(self) -> None:
        self.stack.pop(-1)
        self.minstk.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstk[-1]
```


### Complexity

- Time: O(1) for all operations
- Space: O(2n) = O(n) for the stack structure

