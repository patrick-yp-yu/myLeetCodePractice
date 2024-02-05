# 0739. Daily Temperatures

- tag: MonotonicStack, nextGreaterNum
- URL: https://leetcode.com/problems/daily-temperatures/

# Code 1

- stack: record which day (index)
    - while current temp is higher than previous temps in the stack,
        - it’s warmer, can find a difference ⇒ stack.pop();
    - previous temp = temperatures[ `stk[-1]`  ]
    - `i - top_idx` = the difference between `current day`  &  `the previous day with highest temp`

```python
# 0739. Daily Temperatuers

class Solution:
    def dailyTemperatures(self, temperatures):

        # Close to 0496_nextGreaterElement
        ## Logic
        ## time: O(n), space: O(n)
        ans = [0 for _ in temperatures]
        stk = []

        for i, currTemp in enumerate(temperatures):
            while stk and temperatures[stk[-1]] < currTemp:
                top_idx = stk.pop()
                ans[top_idx] = i - top_idx  # day difference
            stk.append(i)

        return ans

t1 = [73,74,75,71,69,72,76,73]
t2 = [30,40,50,60]
t3 = [30,60,90]

sol = Solution()
ans1 = sol.dailyTemperatures(t1)
print(ans1)
```

## Code 2

- stack keep (temp, index) for each day.
- Only when we finder warmer temp, we can computer the day differences.
    - That’s why we use a while loop.

```python
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Stack save (temp, index)

        ans = [0] * len(temperatures)
        stk = []

        for i, t in enumerate(temperatures):
            while stk and t > stk[-1][0]:
                higherT, higherIdx = stk.pop()
                ans[higherIdx] = (i - higherIdx)
            stk.append([t, i])
        
        return ans
```

```python
temperatures = [73,74,75,71,69,72,76,73]

i=0, currTemp=73
  stk=[]
i=1, currTemp=74
  stk=[[73, 0]]
  prevI=0, prevTemp=73: ans[0]=1
i=2, currTemp=75
  stk=[[74, 1]]
  prevI=1, prevTemp=74: ans[1]=1
i=3, currTemp=71
  stk=[[75, 2]]
i=4, currTemp=69
  stk=[[75, 2], [71, 3]]
i=5, currTemp=72
  stk=[[75, 2], [71, 3], [69, 4]]
  prevI=4, prevTemp=69: ans[4]=1
  prevI=3, prevTemp=71: ans[3]=2
i=6, currTemp=76
  stk=[[75, 2], [72, 5]]
  prevI=5, prevTemp=72: ans[5]=1
  prevI=2, prevTemp=75: ans[2]=4
i=7, currTemp=73
  stk=[[76, 6]]
```

### Complexity

- Time: O(n)
    - At first glance, it may look like the time complexity of this algorithm should be O(n^2) due to while loop
    - However, each element can only be added to the stack once, which means the stack is limited to *N* pops. Every iteration of the while loop uses 1 pop, which means the while loop will not iterate more than *N* times in total, across all iterations of the for loop.
    - An easier way to think about this is that in the worst case, every element will be pushed and popped once. This gives a time complexity of O(2⋅N)=O(N)
- Space: O(n)
    - Note: `ans=[]` does not count towards the space complexity because space used for the output format does not count.