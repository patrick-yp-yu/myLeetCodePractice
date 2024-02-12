# 0456: Find 132 Pattern

- tag: `MonotonicStack`
- URL: https://leetcode.com/problems/132-pattern/description/

<br>

## Code1 Monotonic

1. The first for loop find the minimum number so far. The minimums are candidates of nums[i].
2. Traverse loop
    1. Find the previous greater number using the monotonic stack pattern
        1. pop `all numbers ≤ nums[j]`, the remaining in the stack must be > nums[j]
    2. if stack exist, we found `nums[k]` = the previous greater number of nums[j]
    3. also, need to satisfy `nums[i] < nums[j]`

```python
def find132pattern(self, nums: List[int]) -> bool:

        # 1. Find the minimum number so far => find nums[i] = minimum 
        n = len(nums)
        min_sofar = [nums[0]]   #
        for i in range(1, n):
            min_sofar.append( min(min_sofar[i-1], nums[i]))   # prev_num vs curr_num
        # print(f"min_sofar={min_sofar}")

        # 2. Find the previous greater => nums[k] < nums[j]
        stack = []              # save index
        for j in range(len(nums)):
            while stack and nums[stack[-1]] <= nums[j]: # pop numbers <= nums[j]
                stack.pop()
            
            # Condition1: nums[k] < nums[j]
            # if stack exist => found the previous greater of nums[j] = nums[stack[-1]] = nums[k] 
            # Condition2. 
            # also, need to satisfy   nums[i] < nums[j]
            if stack and min_sofar[stack[-1]] < nums[j]:
                return True
            
            stack.append(j)
        
        return False
```

### Complexity

- Time: O(n)
- Space: O(n) for stack

### Reference:

- [https://leetcode.com/discuss/study-guide/2347639/A-comprehensive-guide-and-template-for-monotonic-stack-based-problems](https://leetcode.com/discuss/study-guide/2347639/A-comprehensive-guide-and-template-for-monotonic-stack-based-problems)

<br>

## Code2

- Same idea as code1.
- Differences are the order of comparison
    - `if nums[j] > min_sofar[j]:`     to find  if nums[j] > nums[i] exist,
    - Because we have the min_sofar array, find greater number to meet `nums[i] < nums[k]`
    - Use `if stack and stack[-1] < nums[j]:` to check `nums[k] < nums[j]`

```python
def find132pattern_1(self, nums: List[int]) -> bool:
        
        # 1. Find the minimum number so far => find nums[i]
        n = len(nums)
        min_sofar = [nums[0]]   #
        for i in range(1, n):
            min_sofar.append( min(min_sofar[i-1], nums[i]))   # prev_num vs curr_num
        print(f"min_sofar={min_sofar}")

        # 2. Find the previous greater => nums[k] < nums[j]
        stack = []  # save number
        for j in range(n-1, -1, -1):        # idx: [n-1 to 0]
            print(f"idx={j}: n_j={nums[j]} vs n_i={min_sofar[j]}")
            if nums[j] > min_sofar[j]:     # if nums[j] > nums[i] exist, 

                while stack and stack[-1] <= min_sofar[j]:
                    stack.pop()             # pop numbers <= min_sofar 

                if stack and stack[-1] < nums[j]:
                    print(f"  stack={stack}")
                    print(f"  n_k:{stack[-1]} vs n_j:{nums[j]} => Found pattern")
                    return True
                stack.append(nums[j])
        
        return False
```

### Complexity

- Time: O(n)
- Space: O(n)

### Reference:

- [https://www.youtube.com/watch?v=3DgzupIuh4s&t=310s](https://www.youtube.com/watch?v=3DgzupIuh4s&t=310s)