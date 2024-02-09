# 0907. Sum of Subarray Minimums

- tag: MonotonicStack
- URL: https://leetcode.com/problems/sum-of-subarray-minimums/


## Code1 Brute Force ⇒ Time Limit Exceeded

- Brute force will need O(n^2) time. Computing the ranges from index i to j is time-consuming.

```python
# Brute force: O(n^2) => Time Limit Exceeded
    def sumSubarrayMins(self, arr: List[int]) -> int:
        sum_min = 0
        for i in range(len(arr)):           # starting point
            for j in range(i, len(arr)):    # end point
                # subarrary = from index i to j
                sum_min += min(arr[i:j+1])
        
        return sum_min % (10 **9 + 7)
```

### Complexity

- Time: O(n^2)
- Space: O(n)

---

### monotonic increasing

- the elements in the stack are not decreasing
- encounter a smaller number, then change stack_top
- push larger number into stack

```python
nums = [5,3,1,2,4]

while curr_val < stk_top of a monotonic increasing:
		pop(stk_top)
		push(curr_val)
else: # curr >= stk_top
		push(curr_val)

i = 0, stk = [5]
i = 1, stk = [3] 3 < 5
i = 2, stk = [1] 1 < 3
i = 3, stk = [1, 2]
i = 4, stk = [1, 2, 4]

[1, 2, 4] = monotonic increasing
```

<br>

## Code2

- Idea: when you encounter the minimum number x, x = min(any subarray that contains the minimum number x)
    - the subarrays (that includes x) ⇒ the minimum number will be= x
    - contribute to the total sum of minimum =  x * ( the count of the subarrays that include x)
- How to find the count of the subarrays that include x?
    - min_index = the index of the minimum number
    - (min_index - left_boundary) * ( right_boundary - min_index)
    - left_boundary = index of (previous smaller number)
    - right_boundary = index of (next smaller number)
    
- The range of subarrays keep changes. Every time you encounter a smaller number, the smaller number will be push into a stack. And, we find the contribution of the smaller number to the overall sum.
- In the code, when encounter new smaller number, we compute the contribution of the previous number.

### Another Interpretation

```python
arr = [6,1,2, 7,8, 4, 5, 3,9]

if 6 is a minimum => subarray  = [6]
if 1 is a minimum => subarrays = any subarrays contains 1
if 4 is a minimum => subarrys = 
left subarrays  = [7,8,4], [8,4], [4]
right subarrays = [7,8,4,5], [8,4,5], [4,5] 

To find contribution of number 4, 
we will find out until meet next smaller number 3
count of left subarrays  = index_(4) - index_(previous smaller number=2) = 5-2=3
count of rightt subarrays= index_(next smaller number=3) - index_(4)= 7-5=2
contribution of 4 = 4 * (3*2) = (number 4) * (subarray counts = 6) 
```


```python
# Monotonic Stack
    def sumSubarrayMins(self, arr: List[int]) -> int:

        sum_min = 0 
        stack = []      # save index of smaller num

        for i, num in enumerate(arr):
            # When encounter a smaller num, push into stack
            # Compute the contribution of the previous num to the sum of minimums
            while stack and arr[i] <= arr[stack[-1]]:
                prev_idx = stack.pop()
                left_bound = stack[-1] if stack else -1
                right_bound = i

                # count the previous contribution
                count = (prev_idx - left_bound) * (right_bound - prev_idx)  # number of subarrys contain
                sum_min += count * arr[prev_idx]
            stack.append(i)

        # Process the remaining in the stack
        while stack:
            prev_idx = stack.pop()
            left_bound = stack[-1] if stack else -1
            right_bound = len(arr)
            count = (prev_idx - left_bound) * (right_bound - prev_idx) 
            sum_min += count * arr[prev_idx]

        return sum_min % (10 **9 + 7)     
        # Time: O(n), Space: O(n)
```


### Complexity

- Time: O(n)
- Space: O(n)