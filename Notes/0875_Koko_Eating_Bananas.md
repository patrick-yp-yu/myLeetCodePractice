# 0875. Koko Eating Bananas

- tag: `BinarySearch`
- URL: https://leetcode.com/problems/koko-eating-bananas/

## Thinking

1. `Input: piles = [3,6,7,11], h = 8`
    - if eating speed = 11, only need 4 hours to finish
    - if eating speed = 1, need (3+6+7+11) hours to finish, which is > 8. Koko will be caught by guard. 
    - mid = 11/2= 5 = eating speed ,  need [1+ 2+2+3] = 8 hours, still cannot finish in time. 
2. KoKo eating speed is ranging from [0, max(piles)]
    - We are using binary search to decide the eating speed, and Koko prefer eat slowly .
    - ⇒ we try to find the minimum speed k=(mid) between range[0, max(piles)] ⇒ use binary search
3. Need to understand the question, and convert to binary search problem. 
    - range = [0, max(piles)] = [l, r]
    - mid = adjustable eating speed ⇒ try to find the minimum eating speed that can finish all in time.

<br>

## Code1

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

<br>

## Code2

- We try to find the minimum speed k between range[0, max(piles)] ⇒ use binary search find k
- Convert unsorted array to FFTTT pattern, find the 1st true pattern

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