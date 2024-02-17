# 0441. Arranging Coins

- tag: `BinarySearch`
- URL: https://leetcode.com/problems/arranging-coins/description/

<br>

## Code1

- Use `cosinSum ≤ n`  to judge if the last row can complete, or incomplete
- mid range = [1 ~ n]
- the l, r start from the outside of the mid range

```python
class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        # Sum of completed rows = Sum of Consecutive Numbers
        def coinSum(i):
            return i * (i+1) / 2

        # maximization template, return the last True, TT'T' FF
        # if coinSum <= given n, last row can complete, return true
        # if coinSum > given n, last row is incomplete, return false
        l, r = 0, n + 1         #  
        while (l + 1) < r:
            mid = l + (r - l) // 2
            print(f"l={l}, r={r}: mid={mid}")
            if coinSum(mid) <= n:
                l = mid
                print(f"   can complete, completed rows={l}")
            else:
                r = mid
                print(f"   incomplete, r={r}")
        
        print(f"End loop: l={l}, r={r}: mid={mid}")
        return l
```

```python
Input: n = 5

l=0, r=6: mid=3
   incomplete, r=3
l=0, r=3: mid=1
   can complete, completed rows=1
l=1, r=3: mid=2
   can complete, completed rows=2
End loop: l=2, r=3: mid=2

######
Input: n = 8

l=0, r=9: mid=4
   incomplete, r=4
l=0, r=4: mid=2
   can complete, completed rows=2
l=2, r=4: mid=3
   can complete, completed rows=3
End loop: l=3, r=4: mid=3
```

### Complexity

- Time: O(log n)
- Space:  O(1)

### Reference:

- [https://leetcode.com/discuss/study-guide/2371234/An-opinionated-guide-to-binary-search-(comprehensive-resource-with-a-bulletproof-template)#441-arranging-coins](https://leetcode.com/discuss/study-guide/2371234/An-opinionated-guide-to-binary-search-(comprehensive-resource-with-a-bulletproof-template)#441-arranging-coins)

<br>
