# 0162. Find Peak Element

- tag: `BinarySearch`
- URL: https://leetcode.com/problems/find-peak-element/description/

## Code1

- FFTF, The monotonic function will check `nums[idx] > nums[idx +1]`
- Peak element will have `FTF`  pattern, `nums[i-1] < nums[i] > nums[i+1]`

```python
class Solution:
    # Find 1st index of peak element using binary search
    # FFTF, FTFFFTF
    def findPeakElement(self, nums: List[int]) -> int:
        
        def isGreater(nums, idx):
            if idx == len(nums) -1:     # nums[n-1] will always > nums[n](=-inf)
                return True
            return nums[idx] > nums[idx + 1]

        lo, hi = -1, len(nums)
        while (lo + 1) < hi:
            mid = lo + (hi - lo) // 2
            if isGreater(nums, mid):
                hi = mid
            else:
                lo = mid
        # return 1st idx of peak element
        return hi
```

### Complexity

- Time: O(log n)
- Space: O(1)

### Reference:

- [https://leetcode.com/discuss/study-guide/2371234/An-opinionated-guide-to-binary-search-(comprehensive-resource-with-a-bulletproof-template)/1524817](https://leetcode.com/discuss/study-guide/2371234/An-opinionated-guide-to-binary-search-(comprehensive-resource-with-a-bulletproof-template)/1524817)
