# 0744. Find Smallest Letter Greater Than Target

- tag: `BinarySearch`
- URL: https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/


<br>

## Code1 Binary Search

```python
class Solution:
    # Binary Search
    # Find smallest letter = Find first pattern; Conditions: > target
    def nextGreatestLetter_1(self, letters: List[str], target: str) -> str:
        
        l, r = -1, len(letters)
        while (l + 1) < r:
            mid = l + (r - l) // 2
            if (letters[mid] > target):     # FF'T'TT
                # target at left, move r
                r = mid
            else:
                l = mid
        
        # r = len(letter) => target not found 
        return letters[r] if r != len(letters) else letters[0]
        # Time: O(log n), Space: O(1)
```

### Complexity

- Time: O(log n)
- Space: O(1)

### Reference:

- [https://leetcode.com/discuss/study-guide/2371234/An-opinionated-guide-to-binary-search-(comprehensive-resource-with-a-bulletproof-template)](https://leetcode.com/discuss/study-guide/2371234/An-opinionated-guide-to-binary-search-(comprehensive-resource-with-a-bulletproof-template))

<br>

## Code2 Binary Search 2


```python
# Binary Search 2
    def nextGreatestLetter_2(self, letters: List[str], target: str) -> str:
        
        if target < letters[0] or letters[-1] <= target:     # boundary conditions
            return letters[0]

        l, r = 0, len(letters) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if letters[mid] > target:    # target at left, move r 
                r = mid - 1
            else: # letters[mid] <= target; need to find letter > target; target at right
                l = mid + 1
        return letters[l]
        # Time: O(log n), Space: O(1)
```

### Complexity

- Time: O(log n)
- Space: O(1)


<br>

## Code3 Python Bisect

```python
# Python Bisect
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # need to > target =>  
        # bisect_right(letters, target) return index after finding target
        
        idx_right = bisect.bisect_right(letters, target)
        if idx_right > len(letters) -1:     # boundary conditions
            return letters[0]
        return letters[idx_right]
```