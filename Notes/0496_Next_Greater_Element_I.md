# 0496. Next Greater Element I

- tag: MonotonicStack, nextGreaterNum
- URL: https://leetcode.com/problems/next-greater-element-i/

# Think

To remember the greater numbers that has traversed ⇒ Stack

1. Use stack,
2. pop `while curr num > stack.top`  , 
    1. map the popped element to current num, 
    2. current num = the next greater number of the popped element
3. Traverse nums1.  Find the next greater element of each number through the saved dictionary.

The question is an typical example of **monotonous stack**

# Code 1

1. use stack to find the next greater number. 
- `while curr num > stack.top`
    - `current num`  = the next greater number of `stack[-1]`
1. go through nums1, look up dictionary to find the next greater number 

- Uses the monotonic stack
    - when encounter number > stack.top(), pop the stack
    - the next greater number of stack.top() = the current number

```python
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # 1. record (k, v) = (curr num, next greater num)
        table = defaultdict(int)    
        stack = []
        for i, x in enumerate(nums2):
            # 2. when currValue > stackedValue => Found the next greater 
            print(f"i={i}, x={x}")
            print(f"  stk={stack}")
            while len(stack) > 0 and stack[-1] < x: 
                print(f"  next greater number of {stack[-1]} = {x}")
                table[ stack.pop() ] = x
            stack.append(x)     # push

        # 3. Find the next greater element based on nums1
        ans = []
        for i, x in enumerate(nums1):
            if x in table:
                ans.append(table[x])
            else:
                ans.append(-1)
        return ans   
    # Time: O( nums1 + nums2) = O(m + n)
    # Space: O(n)
```


```python
nums1 = [4,1,2], nums2 = [1,3,4,2]

i=0, x=1
  stk=[]
i=1, x=3
  stk=[1]
  next greater number of 1 = 3
i=2, x=4
  stk=[3]
  next greater number of 3 = 4
i=3, x=2
  stk=[4]
```

### Complexity

- Time: O( len(nums1) + len(nums2)) = O(n)
- Space: O(n)