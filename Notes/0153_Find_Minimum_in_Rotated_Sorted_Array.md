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
- [1, 2, 3, 4, 5] is sorted, `nums[-1] >= each element`
- [3, 4, 5, 1, 2] is rotated. The pivot point = the minimum element in the rotated array.
- [F, F, F, T, T]  Let’s change the question. Find 1st index where `nums[mid] <= nums[-1]`
    - The question becomes to find 1st index and we can apply binary search.
- if `nums[mid] <= nums[-1]:`
    - FFF'T'T, the mid index is currently inside the right-half of the pivot, so we need to move r to find the left-half
- if `nums[mid] > nums[-1]:`
    - The mid index is currently inside the left-hlaf of the pivot, so we need to move l to find the right-half.

```python
# [3,4,5,1,2], Change problem to find 1st index where "nums[mid] <= nums[-1]"
    #  F,F,F,T,T   F = left side of the pivot, T = right side of the pivot
    def findMin(self, nums: List[int]) -> int:
        l, r = -1, len(nums) 
        while (l + 1) < r:
            mid = l + (r - l) // 2
            if nums[mid] <= nums[-1]:   # FFF'T'T, inside the right-half of the pivot, move r 
                r = mid
            else:                       # > nums[-1], inside the left-half, move l
                l = mid
        # print(f"l={l}, r={r}")          # return the minimum element, not index
        return nums[r]
```

### Complexity

- Time: O(log n)
- Space: O(1)

### Reference:

- [https://leetcode.com/discuss/study-guide/2371234/An-opinionated-guide-to-binary-search-(comprehensive-resource-with-a-bulletproof-template)/1524817](https://leetcode.com/discuss/study-guide/2371234/An-opinionated-guide-to-binary-search-(comprehensive-resource-with-a-bulletproof-template)/1524817)