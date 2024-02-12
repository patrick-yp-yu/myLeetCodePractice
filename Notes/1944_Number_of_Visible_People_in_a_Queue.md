# 1944. Number of Visible People in a Queue

- tag: MonotonicStack
- URL: https://leetcode.com/problems/number-of-visible-people-in-a-queue/description/

<br>

## Code1

- A person can see another person to their right if everybody in between is shorter than both of them.
- if person_i can see person_j
    - height_i ⇒ index from `i+1` to `j-1` , heights shorter than both height_i & height_j ⇒ height_j
- `while heights[stack[-1]] <= h`
    - Take care the next greater height.
    - When current_height is larger than stackTop, current_height can be seen by the stackTop.
- `if stack:`
    - Take care the previous greater number. The previous greater height can see current_height.
    - Use if. Not while. If previous greater number exist, the previous greater number will block his left-hand side to see the shorter height.

```python
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        
        stack = []  # save index
        ans = [0] * len(heights)    # default = see 0 people

        for i, h in enumerate(heights):
            # Find the next greater_height for current_height
            # stack element = strictly decreasing
            # print(f"i={i}, h={h}")
            while stack and  heights[stack[-1]] <= h:
                shorter_idx = stack.pop()
                ans[shorter_idx] += 1
                # print(f"  NG:{heights[shorter_idx]} can see {h}, ans={ans}")

            # Find previous greater 
            if stack:
                ans[stack[-1]] += 1
                # print(f"  PG:{heights[stack[-1]]} can see {h}, ans={ans}")

            stack.append(i)
        
        return ans
```

```python
i=0, h=10
i=1, h=6
  PG:10 can see 6, ans=[1, 0, 0, 0, 0, 0]
i=2, h=8
  NG:6 can see 8, ans=[1, 1, 0, 0, 0, 0]
  PG:10 can see 8, ans=[2, 1, 0, 0, 0, 0]
i=3, h=5
  PG:8 can see 5, ans=[2, 1, 1, 0, 0, 0]
i=4, h=11
  NG:5 can see 11, ans=[2, 1, 1, 1, 0, 0]
  NG:8 can see 11, ans=[2, 1, 2, 1, 0, 0]
  NG:10 can see 11, ans=[3, 1, 2, 1, 0, 0]
i=5, h=9
  PG:11 can see 9, ans=[3, 1, 2, 1, 1, 0]
```

### Complexity

- Time: O(n)
- Space: O(n) for stack

### Reference:

- [https://leetcode.com/discuss/study-guide/2347639/A-comprehensive-guide-and-template-for-monotonic-stack-based-problems](https://leetcode.com/discuss/study-guide/2347639/A-comprehensive-guide-and-template-for-monotonic-stack-based-problems)
