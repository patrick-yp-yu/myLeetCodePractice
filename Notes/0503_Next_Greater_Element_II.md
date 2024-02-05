# 0503. Next Greater Element II

- tag: MonotonicStack, nextGreaterNum
- URL: https://leetcode.com/problems/next-greater-element-ii/

# Logic

- The elements saved in the stack will be monotonic
    - here, store index in the stack,
    - if `nums[ stack[-1]]`  < `current number`
        - ⇒ found the next greater number, and can do `stack.pop()`
- 1st for loop, save index in the stack,
    - `nums[stacked_index]` means that it did not find the next greater element yet.
- 2nd for loop,
    - compare  stack & nums
    - no push new element into the stack

## Related Question

- 0496. Next Greater Element I

- 0503 is given a circular array.

<br>

# Sol1

```python
# 0503 nextGreaterElements

class Solution:
    def nextGreaterElements(self, nums):
        ### Logic ###
        ## 1. 2 pass with stack 
        ## 2. In the 1st loop, find possible NGE (next greater element) in nums
        ## 3. In 2nd pass, some numbers have not found NGE. Find in a circular array. 
        ## Time: O(n)   Space: O(n)
         
        # print(f'0, nums={nums}')
        ans = [-1] * len(nums)
        stack = [] # store the index of nums
        for i, curr in enumerate(nums):        # step2
            while stack and nums[stack[-1]]< curr:
                ans[stack.pop()] = curr
                # print(f'{i}, ans={ans}, \ts={stack}')
            stack.append(i) # push the index
            # print(f'{i}, ans={ans}, \ts={stack}')

        # print('2nd pass:')
        for i, curr in enumerate(nums):         # step3
            while stack and nums[stack[-1]] < curr:
                ans[stack.pop()] = curr 
                # print(f'{i}, ans={ans}, s={stack}')
        
        return ans

nums1 = [1,2,3,4,3]
nums2 = [1,2,1]
nums3 = [100,1,11,1,120,111,123,1,-1,-100] # expected = [120,11,120,120,123,123,-1,100,100,100]
nums4 = [10, 1, 2, 12, 1, 3, 2]    
#expect=[12, 2,12, -1, 3, 10,10]

sol1 = Solution()
ans1 = sol1.nextGreaterElements(nums4)
print(ans1)
```

 

Sol1 test case

```python
0, nums=[10, 1, 2, 12, 1, 3, 2]
0, ans=[-1, -1, -1, -1, -1, -1, -1],    s=[0] elements= [10] 
1, ans=[-1, -1, -1, -1, -1, -1, -1],    s=[0, 1], elements = [10,1]
2, ans=[-1, 2, -1, -1, -1, -1, -1],     s=[0], elements = [10]
2, ans=[-1, 2, -1, -1, -1, -1, -1],     s=[0, 2]
3, ans=[-1, 2, 12, -1, -1, -1, -1],     s=[0]
3, ans=[12, 2, 12, -1, -1, -1, -1],     s=[]
3, ans=[12, 2, 12, -1, -1, -1, -1],     s=[3]
4, ans=[12, 2, 12, -1, -1, -1, -1],     s=[3, 4]
5, ans=[12, 2, 12, -1, 3, -1, -1],      s=[3]
5, ans=[12, 2, 12, -1, 3, -1, -1],      s=[3, 5]
6, ans=[12, 2, 12, -1, 3, -1, -1],      s=[3, 5, 6]
2nd pass:
0, ans=[12, 2, 12, -1, 3, -1, 10], s=[3, 5]
0, ans=[12, 2, 12, -1, 3, 10, 10], s=[3]
```


<br>

# Sol2

```python
def nextGreaterElements2(self, nums):
        # print(f'0, nums={nums}')
        ans = [-1 for _ in nums]
        stack = []
        for i, curr in enumerate(nums):
            while stack and stack[-1][1] < curr:
                idx, val = stack.pop() 
                ans[idx] = curr
                # print(f'{i}, ans={ans}, \ts={stack} vs {curr}')
            stack.append((i, curr)) # push current index & val
            # print(f'{i}, ans={ans}, \ts={stack} push {curr}')
        
        # Find the next greater element for the number remaining in the stack 
        # print('2nd pass:')
        for i, curr in enumerate(nums):
            while stack and stack[-1][1] < curr:
                idx, val = stack.pop() 
                ans[idx] = curr
                # print(f'{i}, ans={ans}, \ts={stack} vs {curr}')
        return ans
```

sol2 test case:

```python
0, nums=[10, 1, 2, 12, 1, 3, 2]
0, ans=[-1, -1, -1, -1, -1, -1, -1],    s=[(0, 10)] push 10
1, ans=[-1, -1, -1, -1, -1, -1, -1],    s=[(0, 10), (1, 1)] push 1
2, ans=[-1, 2, -1, -1, -1, -1, -1],     s=[(0, 10)] vs 2
2, ans=[-1, 2, -1, -1, -1, -1, -1],     s=[(0, 10), (2, 2)] push 2
3, ans=[-1, 2, 12, -1, -1, -1, -1],     s=[(0, 10)] vs 12
3, ans=[12, 2, 12, -1, -1, -1, -1],     s=[] vs 12
3, ans=[12, 2, 12, -1, -1, -1, -1],     s=[(3, 12)] push 12
4, ans=[12, 2, 12, -1, -1, -1, -1],     s=[(3, 12), (4, 1)] push 1
5, ans=[12, 2, 12, -1, 3, -1, -1],      s=[(3, 12)] vs 3
5, ans=[12, 2, 12, -1, 3, -1, -1],      s=[(3, 12), (5, 3)] push 3
6, ans=[12, 2, 12, -1, 3, -1, -1],      s=[(3, 12), (5, 3), (6, 2)] push 2
2nd pass:
0, ans=[12, 2, 12, -1, 3, -1, 10],      s=[(3, 12), (5, 3)] vs 10
0, ans=[12, 2, 12, -1, 3, 10, 10],      s=[(3, 12)] vs 10

[12, 2, 12, -1, 3, 10, 10]
```

<br>

# Sol3

- for & while loop are the same
- circular array ⇒ `cir_nums = nums * 2`
- extend nums for circular array, so no need to 2-pass in sol2

```python
# Improved Sol2
    def nextGreaterElements3(self, nums: List[int]) -> List[int]:
        
        N = len(nums)
        cir_nums = nums * 2
        ans = [-1 for _ in nums]
        stack = []
        
        for i, curr in enumerate(cir_nums):
            while stack and stack[-1][1] < curr:
                idx, val = stack.pop()
                ans[idx] = cir_nums[i]
            
            if i < N:
                stack.append((i, curr))
        
        return ans
```

## Reference

Watch the link for Sol3

[https://www.youtube.com/watch?v=SfNlyzNEKyg&ab_channel=Knapsak](https://www.youtube.com/watch?v=SfNlyzNEKyg&ab_channel=Knapsak)