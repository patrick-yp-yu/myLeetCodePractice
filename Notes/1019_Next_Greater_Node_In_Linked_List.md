# 1019. Next Greater Node In Linked List

- tag: MonotonicStack
- URL: https://leetcode.com/problems/next-greater-node-in-linked-list/description/

## Thinking

1. Find the next greater number 
    1. Strictly increasing: [1, 2, 3, 4, 5] ⇒ ans = [2, 3, 4, 5, 0]
    2. Strictly decreasing: [5,4,3,2,1] ⇒ ans = [0, 0, 0, 0, 0]
    3. harder case:  [ 5,4,1, 7,9]

---

## Code1 Monotonic stack

- Use stack
    1. the elements in the stack are strictly decreasing
    2. when encounter a larger number, `current_num > stack[-1]`  
        1. the next greater number of `stack[-1]` = current_num, stack.pop()
        2. need to compare current_num with previous numbers in the stack, until    `current_num <= stack[-1]`  , which ends the while loop

```python
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        # Read linked-list into list
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        ans = [0] * len(nums)   # default = 0
        stack = []      # record index

        for i, num in enumerate(nums):
            # when encouter a larger number, check if it's a next greater number
            # keep compare current_num vs stack[-1]
            while stack and num > nums[stack[-1]]:
                idx_smaller = stack.pop()
                ans[idx_smaller] = num
            stack.append(i)

        return ans
```

### Complexity

- Time: O(n)
- Space: O(n) for stack

### Reference:

- [https://www.youtube.com/watch?v=xDeOQXYStWE](https://www.youtube.com/watch?v=xDeOQXYStWE)

