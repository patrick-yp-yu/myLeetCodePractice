# 0278. First Bad Version

- tag: `BinarySearch`
- URL: https://leetcode.com/problems/first-bad-version/description/

<br>


## Code1 Binary Search way 1

- All the versions after a bad version are also bad. 
- Once isBadVersion() return true, all the version after return true. The pattern looks like "FFFTTTT"
- We need to the find the 1st true using binary search. 
- `isBadVersion(mid) = True`
  - When isBadVersion() return true, the right-half will be all true. The 1st True will be at left-half. ==> move hi
- `isBadVersion(mid) = False`
  - The 1st True will be at right-half. ==> move lo

```python
class Solution:
    # Return true, when it is a badversion. isBadVersion(5) = true
    # Find first true pattern, FFFTTTT => hi is the valid answer
    def firstBadVersion(self, n: int) -> int:
        
        lo, hi = 0, n       # search space= [1 ~ n]
        while (lo + 1 < hi):
            mid = lo + (hi - lo) // 2
            # print(f"lo={lo}, mid={mid}, hi={hi}")
            if isBadVersion(mid) == True:
                hi = mid
                # print(f"  hi = {hi}")                
            else:
                lo = mid
                # print(f"  lo = {lo}")  

        # print(f"ans={hi}")
        return hi
```

```python
Input: n = 5, bad = 4

lo=0, mid=2, hi=5
  lo = 2
lo=2, mid=3, hi=5
  lo = 3
lo=3, mid=4, hi=5
  hi = 4
ans=4
```

### Reference:

- [https://leetcode.com/discuss/study-guide/2371234/An-opinionated-guide-to-binary-search-(comprehensive-resource-with-a-bulletproof-template)](https://leetcode.com/discuss/study-guide/2371234/An-opinionated-guide-to-binary-search-(comprehensive-resource-with-a-bulletproof-template))

### Complexity

- Time: *O*(log*n*)
- Space: *O*(1)

<br>

## Code2 Binary Search way 2

- `l, r = 1, n`   in the actual search space
- `while l <= r:`
    - r = mid - 1
    - l = mid + 1

```python
# Sol2  
    def firstBadVersion(self, n: int) -> int:

        l, r = 1, n         # in the seach space
        while l <= r:
            mid = l + (r - l) // 2
            # print(f"l={l}, mid={mid}, r={r}")
            if isBadVersion(mid) == True:
                r = mid - 1
                # print(f"  T, r = {r}")
            else:
                l = mid + 1
                # print(f"  F, l = {l}")

        # print(f"ans={l}")
        return l
```

```python
Input: n = 5, bad = 4
l=1, mid=3, r=5
  F, l = 4
l=4, mid=4, r=5
  T, r = 3
ans=4

###########
Input: n = 1, bad = 1
l=1, mid=1, r=1
  T, r = 0
ans=1
```


### Complexity

- Time: *O*(log*n*)
- Space: O(1)