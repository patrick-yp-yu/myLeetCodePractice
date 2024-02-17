# 875. Koko Eating Bananas

tag: BinarySearch
URL: https://leetcode.com/problems/koko-eating-bananas/

## Thinking

1. 
2. 

---

## Code1

- 

```python
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Given piles.length <= h, so guarantee that Koko can finish eating all
        # Koko likes to eat slowly => Return the minimum k  (speed)
        # the largest k = max(piles elements)
        # Search from [1 ... max(piles)] => use Binary search

        l, r = 1, max(piles)
        ans = r # Set to max(piles) initial, goal is to find the min

        while l <= r:
            speedK = l + (r - l) // 2

            # Iterate over piles to compute time
            hours = 0
            for p in piles:
                hours += math.ceil(p / speedK)   # round up
            
            if hours <= h:  # Can finish in-time
                ans = min(ans, speedK)
                r = speedK - 1  # try slower speed
            else:
                l = speedK + 1
        
        return ans
        # Time: O( n * log(m)), n = len(piles), m = max(piles)
        # Space: O(1)
```

### Reference:

- [https://www.youtube.com/watch?v=U2SozAs9RzA&ab_channel=NeetCode](https://www.youtube.com/watch?v=U2SozAs9RzA&ab_channel=NeetCode)

### Complexity

- Time: O( n * log(m)), n = len(piles), m = max(piles)
- Space: O(1)

---

## Code2

- 

```python
# Binary search 
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def canFinishInH(piles, speed, h):
            hours = 0
            for p in piles:
                hours += math.ceil(p / speed)
                if hours > h:
                    return False
            return True

        l, r = 0, max(piles)
        while (l + 1) < r:
            mid = l + (r - l) // 2
            if canFinishInH(piles, mid, h):
                r = mid
            else:
                l = mid
        
        return r
```

### Reference:

- [https://leetcode.com/discuss/study-guide/2371234/An-opinionated-guide-to-binary-search-(comprehensive-resource-with-a-bulletproof-template)](https://leetcode.com/discuss/study-guide/2371234/An-opinionated-guide-to-binary-search-(comprehensive-resource-with-a-bulletproof-template))

### Complexity

- Time: O( n * log(m)), n = len(piles), m = max(piles)
- Space: O(1)