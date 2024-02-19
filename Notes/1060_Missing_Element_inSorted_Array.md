# 1060. Missing Element in Sorted Array

- tag: `BinarySearch`
- URL: https://leetcode.com/problems/missing-element-in-sorted-array/

<br>

## Code1 Iteration

- gap_counts = the difference between 2 consecutive number -1
    - nums=[4, 7] ⇒ gap=[5, 6] ⇒ gap_counts = 7-4 -1 =2

```python
class Solution:
    # 1. Iteration: O(n)
    def missingElement_1(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        for i in range(1, n):
            gap_counts = nums[i] - nums[i-1] -1     # #of missed elements
            if  gap_counts >= k:                    # target is inside the gap     
                return nums[i -1] + k
            
            k -= gap_counts                         # target is outsdie the gap, continue

        # When no gap in nums: gap_count=0,  [1,2,3], k=3 => return 6
        return nums[n-1] + k
        # Time: O(n), Space: O(1)
```

### Complexity

- Time: O(n)
- Space: O(1)

### Reference:

- [https://leetcode.com/problems/missing-element-in-sorted-array/editorial/](https://leetcode.com/problems/missing-element-in-sorted-array/editorial/)

<br>

## Code2 Binary Search

- Need to decide
    1. search space 
    2. **the monotonic function**
- Find total numbers of missed elements at index i
    - For a range:`[ nums[0], nums[i] ]`,
    - The total number of integers within the range = `nums[i]- nums[0] + 1`
    - The actual existing integers in nums = `i + 1` , judging from the index.
    - #of missed integers = `nums[i]- nums[0] + 1` - `i + 1` = `nums[i]- nums[0] - i`
- the monotonic function:   `(total numbers of missed elements at index i)  < k`
    - TTTFF pattern
    - The goal is to find the 1st False = the kth missing integer
- **Key point: find element when no gap**
    - `nums[l] + k - missedCountAt(nums, l)`
    - when there is no gap, nums[l] = nums[-1]

```python
# 2. Binary Search
    def missingElement(self, nums: List[int], k: int) -> int:

        def missedCountAt(nums, i):               # #of missed integers at idx
            return nums[i] - nums[0] - i

        l, r = -1, len(nums)
        while l + 1 < r:
            mid = l + (r - l)// 2
            # print(f"l={l}, r={r}: mid={mid}")
            if missedCountAt(nums, mid) < k:
                l = mid
                # print(f"   missedCount={missedCountAt(nums, mid)} < k, move l={l}")
            else: 
                r = mid
        #         print(f"   missedCount={missedCountAt(nums, mid)} > k, move r={r}")
        
        # print(f"End loop. l={l}, r={r}:")
        # print(f"   nums[l]({nums[l]}) + k({k}) - missedCount({missedCountAt(nums, l)})")
        # When no gap in nums: [1,2,3], k=3 => return 6
        # l=2, (nums[l]=3) + 3 - (missedCountAt(l=2)=0)
        return nums[l] + k - missedCountAt(nums, l)
```

```python
Input: nums = [4,7,9,10], k = 1

l=-1, r=4: mid=1
   missedCount=2 > k, move r=1
l=-1, r=1: mid=0
   missedCount=0 < k, move l=0
End loop. l=0, r=1:
   nums[l](4) + k(1) - missedCount(0)
#####

Input: nums = [4,7,9,10], k = 3

l=-1, r=4: mid=1
   missedCount=2 < k, move l=1
l=1, r=4: mid=2
   missedCount=3 > k, move r=2
End loop. l=1, r=2:
   nums[l](7) + k(3) - missedCount(2)

####
Input: nums = [1,2,4], k = 3

l=-1, r=3: mid=1
   missedCount=0 < k, move l=1
l=1, r=3: mid=2
   missedCount=1 < k, move l=2
End loop. l=2, r=3:
   nums[l](4) + k(3) - missedCount(1)
```

### Complexity

- Time: O(log n)
- Space: O(1)

### Reference:

- [https://leetcode.com/discuss/study-guide/2371234/An-opinionated-guide-to-binary-search-(comprehensive-resource-with-a-bulletproof-template)#1060-missing-element-in-sorted-array](https://leetcode.com/discuss/study-guide/2371234/An-opinionated-guide-to-binary-search-(comprehensive-resource-with-a-bulletproof-template)#1060-missing-element-in-sorted-array)