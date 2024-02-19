# 0153. Find Minimum in Rotated Sorted Array

- tag: `BinarySearch`
- URL: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

## Thinking

1. Binary search only works on a sorted array
    - Here, the array is sorted but rotated.

<br>

## Code1 Binary Search 1

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Modified binary search for a rotated sorted array
        n = len(nums)
        l, r = 0, n - 1

        while l <= r:
            # Check if array is rotated.
            if nums[l] <= nums[r]:  # No rotate: array is sorted, "=" for l = r
                print("l={} \t r={}, {} is sorted".format(l,r,nums[l:r+1]))
                return nums[l]

            # Modified binary search. 
            mid = l + (r - l) // 2
            print("l={} m={}  r={}, {}".format(l, mid, r, nums[l: r+1]))
            if nums[l] <= nums[mid]:
                # Normal. Left-half is sorted. Don't contain min.
                l = mid + 1
            else:
                # nums[0] >= nums[mid]
                # Abnormal. Left-half contain min
                r = mid 
        
        return nums[r]
        # Time:O(log n), Space: O(1)
```

```python
nums =[3,4,5,1,2]
l=0 m=2  r=4, [3, 4, 5, 1, 2]
l=3 	   r=4, [1, 2] is sorted

####
nums =[4,5,6,7,0,1,2]
l=0 m=3  r=6, [4, 5, 6, 7, 0, 1, 2]
l=4 	   r=6, [0, 1, 2] is sorted

####
nums =[2,1]
l=0 m=0  r=1, [2, 1]
l=1 	   r=1, [1] is sorted
```

### Complexity

- Time: O(log n)
- Space: O(1)

### Reference:

- [https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/solutions/3417980/without-min-comparison-detailed-explanation/](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/solutions/3417980/without-min-comparison-detailed-explanation/)

<br>

## Code2 Binary Search 2

- The array is sorted but rotated. We need to find the pivot point that separated two sorted parts.
- [1, 2, 3, 4, 5] is sorted; two condition will be satisfied.
    - `nums[l] <= each element`
    - `each element <= nums[-1]`
    - Both condition can help use find the answer.
- [3, 4, 5, 1, 2] is rotated. `The pivot point` = the minimum element in the rotated array.
- [F, F, F, T, T]  Let’s change the question. Find 1st index where satisfy `nums[mid] <= nums[-1]`
    - The question becomes to find 1st index and we can apply binary search.

![rotatedArrayProperty.png](images/rotatedArrayProperty.png)    

### Use `each element <= nums[-1]` to check

- if `nums[mid] <= nums[-1]:`  (monotonically increasing, include `=`)
    - This half is sorted (monotonically increasing). The pivot is not in this half.
    - So, we move r to find the left-half
- if `nums[mid] > nums[-1]:`
    - This half is not sorted (monotonically increasing), the pivot is in this half.

```python
def findMin(self, nums: List[int]) -> int:
        l, r = -1, len(nums) 
        while (l + 1) < r:
            mid = l + (r - l) // 2
            if nums[mid] <= nums[-1]:   # monotonically increasing, pivot in the other half
                r = mid
            else:                       # nums[mid] >= nums[-1], this half contain pivot
                l = mid
        # print(f"l={l}, r={r}")          # return the minimum element, not index
        return nums[r]
```

### Use `nums[l] <= each element` to check

- if `nums[l] <= nums[mid]:`  (monotonically increasing, include `=`)
    - This half is sorted (monotonically increasing). The pivot is not in this half.
    - So, we move r to find the left-half
- if `nums[l] > nums[mid]:`
    - This half is not sorted (monotonically increasing), the pivot is in this half.

```python
def findMin_3(self, nums: List[int]) -> int:
        l, r = -1, len(nums) 
        while (l + 1) < r:
            mid = l + (r - l) // 2
            if nums[l] < nums[mid]:     # monotonically increasing, pivot in the other half
                l = mid
            else:                       # nums[l] >= nums[mid], this half contain pivot
                r = mid
        # print(f"l={l}, r={r}")          # return the minimum element, not index
        return nums[r]
```

### Complexity

- Time: O(log n)
- Space: O(1)

### Reference:

- [https://leetcode.com/discuss/study-guide/2371234/An-opinionated-guide-to-binary-search-(comprehensive-resource-with-a-bulletproof-template)/1524817](https://leetcode.com/discuss/study-guide/2371234/An-opinionated-guide-to-binary-search-(comprehensive-resource-with-a-bulletproof-template)/1524817)