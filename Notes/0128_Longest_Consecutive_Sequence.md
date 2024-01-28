# 0128. Longest Consecutive Sequence

- URL: https://leetcode.com/problems/longest-consecutive-sequence/


## Code1

```python
for n in nums:
		if （n-1) in numsSet: 
		# if left neighbor exist, n is not a head of sequence
		
		else:
		# No left neighbor, could be the start of a sequence
        # find the consecutive number, and check if a longest
```

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Put nums into set
        numSet = set(nums)
        longest = 0

        for n in nums:
            # Check if there is a left neighbor => start of a sequence
            if (n-1) in numSet:
                continue
            
            # no left neighbor
            length = 0 
            while (n + length) in numSet:   # count consecutive sequence
                length += 1
            
            longest = max(longest, length)
        
        return longest
```

### Complexity

- Time: O(n)
- Space: O(n) because of using set()
