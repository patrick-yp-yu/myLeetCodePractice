# 1762. Buildings With an Ocean View

- tag: MonotonicStack
- URL: https://leetcode.com/problems/buildings-with-an-ocean-view/description/

<br>

## Code1 Monotonic Stack ()

- This is a **previous greater type** problem. Find previous greater number ⇒ has ocean view
- The elements are strictly decreasing ⇒ has an ocean view to right

```python
class Solution:
    # Monotonic Stack ()
    # right side = ocean, right side should be smaller to allow a ocean view
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        stack = []  # save index of building

        for i, h in enumerate(heights):
            # if heights in the stack <= current_height, no view => stack.pop
            # stack = building with an ocean view, heights are strictly decreasing
            while stack and heights[stack[-1]] <= h:
                stack.pop()
            stack.append(i)
        
        return stack
        # Time: O(n), Space: O(n) for stack
```



### Complexity

- Time: O(n)
- Space: O(n) for stack

<br>

## Code2 Traverse reversely

```python
# Traverse reversely
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        ans = []
        max_height = 0 
        for i in range(len(heights)-1, -1, -1):  # (start, stop, step)
            # from the last index, curr_height vs max_height
            if heights[i] > max_height:
                max_height = heights[i]
                ans.append(i)
        
        return ans[::-1]
        # Time: O(n), Space: O(1) for max_height variable
```


### Complexity

- Time: O(n)
- Space: O(1)