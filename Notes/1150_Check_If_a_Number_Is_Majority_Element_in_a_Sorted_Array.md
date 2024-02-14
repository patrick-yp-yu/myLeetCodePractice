# 1150. Check If a Number Is Majority Element in a Sorted Array

- tag: `BinarySearch`, `HashTable`
- URL: https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array

## Thinking

1. Majority count need to > (len(nums) /2 )

<br>

## Code1

```python
class Solution:
    # Counter 
    def isMajorityElement_1(self, nums: List[int], target: int) -> bool:
        
        freq = collections.Counter(nums)
        target_count = freq[target]
        
        return True if target_count > (len(nums) /2) else False
        # Time: O(n), Space: O(n)
```


### Complexity

- Time: O(n)
- Space: O(n)

<br>

## Code2 Binary Search (2 pass)



```python
# Binary Search (2 pass)
    def isMajorityElement_2(self, nums: List[int], target: int) -> bool:

        def findFirst(nums, target):    # FF `T`TTT
            l, r = -1, len(nums)
            while (l + 1) < r:
                mid = l + (r - l) // 2
                if nums[mid] >= target: # target at the left-half
                    r = mid
                else:
                    l = mid

            if r == len(nums) or nums[r] != target: # boundary check
                return -1
            return r
        
        def findLast(nums, target):     # TTT 'T' FF
            l, r = -1, len(nums)
            while (l + 1) < r:
                mid = l + (r - l) // 2
                if nums[mid] <= target: # target at the right-half
                    l = mid
                else:
                    r = mid
            
            if l == -1 or nums[l] != target:
                return -1
            return l

        idx_1st = findFirst(nums, target)
        idx_last = findLast(nums, target)
        if idx_1st == -1 or idx_last == -1:     # boundry check
            return False
        diff = idx_last - idx_1st + 1
        return diff > (len(nums) /2 ) 
        # Time: O(log n), Space: O(1)
```

### Reference:

- [https://leetcode.com/discuss/study-guide/2371234/An-opinionated-guide-to-binary-search-(comprehensive-resource-with-a-bulletproof-template)](https://leetcode.com/discuss/study-guide/2371234/An-opinionated-guide-to-binary-search-(comprehensive-resource-with-a-bulletproof-template))

### Complexity

- Time: O(log n)
- Space: O(1)

<br>

## Code3 Binary Search (1 pass)

- We only need to find if there are more than `num.length / 2` instances of `target`, not the exact count of `target`.
- After finding the 1st index of target,  `nums[firstIndex + nums.length / 2]`  should be equal to target

```python
# Binary Search (1 pass)
    # 1. Find the index of 1st target
    # 2. idx + len(nums)/2 => the number should be equal to target if it's majority
    def isMajorityElement(self, nums: List[int], target: int) -> bool:

        def findFirst(nums, target):    # FF `T`TTT
            l, r = -1, len(nums)
            while (l + 1) < r:
                mid = l + (r - l) // 2
                if nums[mid] >= target: # target at the left-half
                    r = mid
                else:
                    l = mid

            if r == len(nums) or nums[r] != target: # boundary check
                return -1
            return r
        
        idx_1st = findFirst(nums, target)
        if idx_1st == -1:   # target not found
            return False
        
        idx_last = idx_1st + int(len(nums) /2 )
        return True if idx_last < len(nums) and nums[idx_last] == target else False
```

<br>

## Code4 Python bisect

- bisect.**bisect_left**(*a*, *x*, *lo=0*, *hi=len(a)*, ***, *key=None*)
    - To insert number x, find the **1st insertion index** in array a and maintain sorted order.
- bisect.**bisect_right**(*a*, *x*, *lo=0*, *hi=len(a)*, ***, *key=None*)
    - To insert number x, find the insertion index in array a which **comes after all existing x**
    - and maintain sorted order.

```python
# Python bisect, find insertion point
    def isMajorityElement(self, nums: List[int], target: int) -> bool:

        idx_1st = bisect_left(nums, target)     # insertion point on left
        idx_last = bisect_right(nums, target)   # insertion point on right
        return (idx_last - idx_1st) > (len(nums) /2 )
```

```python

>>> nums = [10,100,101,101]

>>> bisect.bisect_left(nums, 101) 
2
>>> bisect.bisect_right(nums, 101)  
4

```

### Reference:

- [https://docs.python.org/3/library/bisect.html](https://docs.python.org/3/library/bisect.html)
- [https://github.com/python/cpython/blob/3.12/Lib/bisect.py](https://github.com/python/cpython/blob/3.12/Lib/bisect.py)

### Complexity

- Time: O(log n)
- Space: O(1)