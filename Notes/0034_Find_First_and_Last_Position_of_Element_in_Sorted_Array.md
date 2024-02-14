# 0034. Find First and Last Position of Element in Sorted Array

- tag: `Array`, `BinarySearch`
- URL: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

<br>

# Code1 Thinking

1. What is the difference between this and typical binary search?
    1. Target can show multiple times in the array (≥2)
2. only when `nums[l] == nums[r] == target` , 
    1. we found both the 1st & the last targets.
3. when `nums[mid] == target`,  we need to continually find the left & right boundary for l & r
    1. when `nums[l] or nums[r]  == target` , no need to shrink the boundary 

## Code1

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Binary search
        
        l, r = 0, len(nums) - 1
        
        idx_list = []
        while l <= r:
            mid = l + (r - l) // 2
            print("l={}, r={}, mid={}, {} vs {}=target".format(l, r, mid, nums[mid], target))
            
            if nums[l] == nums[r] == target: # Found the 1st & the last
                return [l, r]
            
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                # nums[mid] == target, found the 1st target
                if nums[l] != target:
                    l += 1
                if nums[r] != target:
                    r -= 1

        # Not found
        return [-1, -1]
```

Example 1:

| index | 0 | 1 | 2 | 3 | 4 |  |
| --- | --- | --- | --- | --- | --- | --- |
| nums | 5 | 7 | 8 | 8 | 10 |  |
|  | l |  | m |  | r | nums[m] ==  mid, l +=1, r -= 1 |
|  |  | l | m | r |  | nums[m] ==  mid, l += 1 |
|  |  |  | l | r |  | nums[l] == nums[r] == target |

Example 2: target = 5

| index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| nums | 4 | 5 | 5 | 7 | 8 | 9 | 10 | 11 |  |
|  | l |  |  | m |  |  |  | r | nums[m] > target, r = m-1,  |
|  | l | m | r |  |  |  |  |  | nums[m] == target, l += 1,  |
|  |  | l | r |  |  |  |  |  | nums[l] == nums[r] == target |

<br>

# Code2 Thinking

- There are 3 conditions
    1. target is at the most left, or the most right of the nums, return [-1, -1]
        1. ex: [3, 4, 5], target = 2
        2. ex: [3, 4, 5], target = 6
    2. target is not in nums. return [-1,-1]
        1. ex [3,6,7],  target = 5
    3. target is within in nums (normal), 
- Just divide into 2 Binary search to find the leftmost & the right most boundary

## Code2 Binary Search way 1

```python
# 2. Two binary search to 
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def LeftTargetIdx(nums, target):
            
            l, r = 0, len(nums) -1
            left_most = -1 # initial value
            
            while l <= r:
                mid = l + (r - l) // 2 
                
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid -1
                else:
                    # nums[mid]== target:
                    left_most = mid # !
                    r = mid - 1
            return left_most
                    
        def RightTargetIdx(nums, target):
            
            l, r = 0, len(nums) -1
            right_most = -1 # initial value
            
            while l <= r:
                mid = l + (r - l) // 2 
                
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid -1
                else:
                    # nums[mid]== target:
                    right_most = mid # !
                    l = mid + 1
            return right_most    
        
        left = LeftTargetIdx(nums, target)
        right = RightTargetIdx(nums, target)
        
        if left == -1 or right == -1: # if == -1, target not found
            ans = [-1, -1]
        else:
            ans = [left, right]
        return ans
```

<br>

# Code3 Binary Search way 2

- Use binary search to `find the 1st target` & `find the last target` separately.
- In findFirst(): find the first occurrence of the target
    - `nums[mid] >= target`:
        - if nums[mid] > target, the target should be in the left-half, move r
        - if nums[mid] == target, it cannot make sure that the number is the 1st target, continually shrink range
    - `nums[mid] < target`: the target should be in the right-half, move l
- In findLast(): find the last occurrence of the target
    - `nums[mid] <= target`:
        - if nums[mid] < target, the target should be in the right-half, move l
        - if nums[mid] == target, it cannot make sure that the number is the last target, continually shrink range
    - `nums[mid] > target`: the target should be in the left-half, move r

```python
##########################
    # 3. Two binary search 2
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def findFirst(nums, target):    # FFF 'T'TT, target = 1st 'T'
            l, r = -1, len(nums)
            while (l + 1) < r:
                mid = l + (r - l) // 2
                print(f"l={l}, r={r}=> mid={mid}: {nums[mid]} vs {target}=target")
                if nums[mid] >= target: # ex: FFF'T' T "T", nums[mid]= "T"
                    r = mid             # 1st target at left-side
                    print(f"   r={r}")
                else:
                    l = mid     # 1st target at right-side
                    print(f"   l={l}")
            
            print(f"loops end. l={l}, r={r}")
            if r == len(nums) or nums[r] != target: # OutOfBoundary or not equal
                return -1
            return  r
        
        def findLast(nums, target):     # TT'T' FFF, target = last 'T'
            l, r = -1, len(nums)
            while (l + 1) < r:
                mid = l + (r - l) // 2
                print(f"l={l}, r={r}=> mid={mid}: {nums[mid]} vs {target}=target")
                if nums[mid] <= target: # ex: "T" T'T' FFF, nums[mid]= "T"
                    l = mid             # the last target 'T' at right-side, move l
                    print(f"   l={l}")
                else:                   # ex: TT'T' FF'F' , nums[mid]= 'F'                     
                    r = mid             # the last target 'T' at left-side, move r
                    print(f"   r={r}")
            
            print(f"loops end. l={l}, r={r}")        
            if l == -1 or nums[l] != target:    # OutOfBoundary or not equal
                return -1
            return l
        
        first = findFirst(nums, target)
        last  = findLast(nums, target)
        return [first, last]
```

- `Input: nums = [5,7,7,8,8,10], target = 8`
- Find first target
    
    
    | index | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 |  |
    | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
    | nums |  | 5 | 7 | 7 | 8 | 8 | 10 |  |  |
    
    ```python
    l=-1, r=6=> mid=2: 7 vs 8=target
       l=2
    l=2, r=6=> mid=4: 8 vs 8=target
       r=4
    l=2, r=4=> mid=3: 8 vs 8=target
       r=3
    loops end. l=2, r=3
    => first target index = r = 3 
    ```
    
- Find last target
    
    ```python
    l=-1, r=6=> mid=2: 7 vs 8=target
       l=2
    l=2, r=6=> mid=4: 8 vs 8=target
       l=4
    l=4, r=6=> mid=5: 10 vs 8=target
       r=5
    loops end. l=4, r=5
    => last target index = l = 4
    ```