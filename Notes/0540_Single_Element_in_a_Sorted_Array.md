# 0540. Single Element in a Sorted Array

- tag: `BinarySearch`
- URL: https://leetcode.com/problems/single-element-in-a-sorted-array/description/

## Thinking

1. Requires O(logn) ⇒ Binary  search
2. Only 1 single element
- length=1: return the element
- length=3: [1,2,2], [1,1,2], either 1st or the last

<br>

## Code1 **Binary Search on Evens Indexes Only**

```python
index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
array=[1, 1, 3, 3, 5, 5, 7, 7, 9, 9]
```

- Elements at the index [0, 2, 4, ..., n - 2] would all have a duplicate element on the right.
    - index i, `i %2 ==0`, `nums[i] == nums[i+1]`
    - if true, all elements on left-half are paired
    - if false, exist a single element  on left-half and it breaks the pattern
- Elements at the index [1, 3, 5, ..., n - 1] would all have a duplicate element on the left.
    - index i, `i %2 ==1`, `nums[i] == nums[i-1]`
- The two condition shows that the element is belong to a pair

```python
class Solution:
    # Binary search on even index:[0,2,4,..]
    # index=[0, 1, 2, 3, 4]
    # array=[2, 2, 3, 3, 4]
    # for even index: nums[i] == nums[i+1] 
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        if len(nums) == 1:          # boundary condition
            return nums[-1]

        l, r = 0, len(nums) - 1
            
        while l < r:
            mid = l + (r - l) // 2
            print(f"l={l}, r={r}:")
            if mid %  2 == 1:       # only check even index
                print("   mid odd, mid - 1")
                mid -= 1
            print(f"   mid={mid}")

            # for even index: nums[i] == nums[i+1], 
            # if true => single on right-half
            # if false => single on left half
            print(f"   nums[mid] vs nums[mid+1] = {nums[mid]} vs {nums[mid + 1]}")
            if nums[mid] == nums[mid + 1]:
                l = mid + 2     # visit next even index
                print(f"   True pair => single at right, move l={l}")                
            else:
                r = mid
                print(f"   False pair => single at left, move r={r}") 

        print(f"l={l}, r={r}")
        return nums[r]
```

```python
nums =[1,1,2]
l=0, r=2:
   mid odd, mid - 1
   mid=0
   nums[mid] vs nums[mid+1] = 1 vs 1
   True pair => single at right, move l=2
l=2, r=2

#########
nums =[1,1,2,2,3]
l=0, r=4:
   mid=2
   nums[mid] vs nums[mid+1] = 2 vs 2
   True pair => single at right, move l=4
l=4, r=4

##########
idx  =[0,1,2,3,4,5,6,7,8]
nums =[1,1,2,3,3,4,4,8,8]

l=0, r=8:
   mid=4
   nums[mid] vs nums[mid+1] = 3 vs 4
   False pair => single at left, move r=4
l=0, r=4:
   mid=2
   nums[mid] vs nums[mid+1] = 2 vs 3
   False pair => single at left, move r=2
l=0, r=2:
   mid odd, mid - 1
   mid=0
   nums[mid] vs nums[mid+1] = 1 vs 1
   True pair => single at right, move l=2
l=2, r=2

######
idx  =[0,1,2,3, 4, 5, 6]
nums =[3,3,7,7,10,11,11]

l=0, r=6:
   mid odd, mid - 1
   mid=2
   nums[mid] vs nums[mid+1] = 7 vs 7
   True pair => single at right, move l=4
l=4, r=6:
   mid odd, mid - 1
   mid=4
   nums[mid] vs nums[mid+1] = 10 vs 11
   False pair => single at left, move r=4
l=4, r=4
```

### Complexity

- Time: O(log (n/2)) = O(log n)
- Space: O(1)

### Reference:

- [https://leetcode.com/problems/single-element-in-a-sorted-array/editorial/](https://leetcode.com/problems/single-element-in-a-sorted-array/editorial/)

### Notes:

- Actually, the solution also works for unsorted array, as long as the array is paired like:
    - `[10, 10, 4, 4, 7, 11, 11, 12, 12, 2, 2]`)

<br>

