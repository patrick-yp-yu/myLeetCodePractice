# 0035. Search Insert Position

- tag: `Array`, `BinarySearch`
- URL: https://leetcode.com/problems/search-insert-position/

# Thinking

- The question requires Time complexity O(log n), ⇒ use binary search
- Another approach:  traverse loop, insert target when target ≤ current number

<br>

# Code1: array

- return the index when target can be inserted
- if  target ≤ current number，we can insert the target

```python
def searchInsert0(self, nums: List[int], target: int) -> int:
        # sorted in ascending 
        
        for i in range(len(nums)):
            if target <= nums[i]:
                return i
        
        # if not found, target is larger than all numbers
        # return len(nums)
        return len(nums)
    # Time O(n)
    # Space O(1)
```

- Time: O(n)
- Space: O(1)

<br>

# Code2: binary search 1

- There are 4 conditions to find the insert position. 
    

```python
def searchInsert(self, nums: List[int], target: int) -> int:
        # Binary search
        # 4 conditions: 
        # 1. target < all elements
        # 2. target == one element
        # 3. target between two elements
        # 4. target > all elements

        l, r = 0, len(nums) -1

        # For condition1:
        if target < nums[l]: return 0

        while l <= r:
            mid = l + (r - l) // 2
            # print("l={}, r={}, mid={}, {} vs {}=target".format(l, r, mid, nums[mid], target))

            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                # For condition2
                return mid

				# For condition 3, 4: return l or (r+1)
        return l
    # Time O(log n)
    # Space O(1), because only need variables l, r, mid
```

```jsx
Input: nums = [1,3,5,6], target = 5 => target == one element

l=0, r=3, mid=1: 3 vs 5=target
l=2, r=3, mid=2: 5 vs 5=target

###########
Input: nums = [1,3,5,6], target = 2 => target between two elements

l=0, r=3, mid=1: 3 vs 2=target
l=0, r=0, mid=0: 1 vs 2=target
loops end. l=1, r=0

###########
Input: nums = [1,3,5,6], target = 7 => target > all elements

l=0, r=3, mid=1: 3 vs 7=target
l=2, r=3, mid=2: 5 vs 7=target
l=3, r=3, mid=3: 6 vs 7=target
loops end. l=4, r=3
```

<br>

# Code3: binary search 2

- Search space = [0,1, ~ n-1]
- For the template, the `l, r = -1, len(nums)` = start from outside of the boundary
- The binary search use the `findFirstTarget` pattern

```python
# Binary Search 2 => FFTTT => minimization type: find first true
    def searchInsert(self, nums: List[int], target: int) -> int:

        # candidates index = [0 ~ len(nums)], len(nums) for "target > all elements"        
        l, r = -1, len(nums)    
        while (l + 1) < r:
            mid = l + (r - l) // 2
            print(f"l={l}, r={r}, mid={mid}: {nums[mid]} vs {target}=target")
            if target <= nums[mid]:
                r = mid     # pick left side, move r=mid
            else:
                l = mid     # pick right side, move l=mid
        print(f"loops end. l={l}, r={r}")
        return r
```

```python
Input: nums = [1,3,5,6], target = 5 => target == one element

l=-1, r=4, mid=1: 3 vs 5=target
l= 1, r=4, mid=2: 5 vs 5=target
loops end. l=1, r=2

###########
Input: nums = [1,3,5,6], target = 2 => target between two elements

l=-1, r=4, mid=1: 3 vs 2=target
l=-1, r=1, mid=0: 1 vs 2=target
loops end. l=0, r=1

###########
Input: nums = [1,3,5,6], target = 7 => target > all elements

l=-1, r=4, mid=1: 3 vs 7=target
l= 1, r=4, mid=2: 5 vs 7=target
l= 2, r=4, mid=3: 6 vs 7=target
loops end. l=3, r=4
```

<br>

# Code4 Python Bisect
 
```python
# Python Bisect
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)
```