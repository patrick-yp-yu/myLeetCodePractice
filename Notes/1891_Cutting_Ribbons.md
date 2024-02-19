# 1891. Cutting Ribbons

- tag: `BinarySearch`
- URL: https://leetcode.com/problems/cutting-ribbons/

## Related Questions

**0875. Koko Eating Bananas**

<br>

## Code1 Binary Search (maximization pattern)

```python
class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        
        def canObtainK(ribbons, length, k):   # wheither can obtain k ribbons
            counts = 0
            for r in ribbons:
                counts += r // length   # cut each ribbon to length
                print(f"   counts += {r}//{length} = {counts}")
                if counts >= k:
                    return True         # can reach k counts
            
            return False

        ####  maximization, find the largest True;  TTTTFF
        l, r = 0, max(ribbons) + 1      # valid range = [1, max(ribbons)]; l,r start from outside
        while l + 1 < r:
            mid = l + (r - l) // 2
            print(f"l={l}, r={r}: mid={mid}")
            if canObtainK(ribbons, mid, k) == True:      # can reach k counts
                l = mid
                print(f"   Can obtain. move l={l}")
            else:
                r = mid
                print(f"   Cannot obtain. move r={r}")
        print(f"End. l={l}, r={r}: mid={mid}")
        return l
```

```python
ribbons = [9,7,5], k = 3

l=0, r=10: mid=5
   counts += 9//5 = 1
   counts += 7//5 = 2
   counts += 5//5 = 3
   Can obtain. move l=5
l=5, r=10: mid=7
   counts += 9//7 = 1
   counts += 7//7 = 2
   counts += 5//7 = 2
   Cannot obtain. move r=7
l=5, r=7: mid=6
   counts += 9//6 = 1
   counts += 7//6 = 2
   counts += 5//6 = 2
   Cannot obtain. move r=6
End. l=5, r=6: mid=6

####
ribbons = [7,5,9], k = 4

l=0, r=10: mid=5
   counts += 7//5 = 1
   counts += 5//5 = 2
   counts += 9//5 = 3
   Cannot obtain. move r=5
l=0, r=5: mid=2
   counts += 7//2 = 3
   counts += 5//2 = 5
   Can obtain. move l=2
l=2, r=5: mid=3
   counts += 7//3 = 2
   counts += 5//3 = 3
   counts += 9//3 = 6
   Can obtain. move l=3
l=3, r=5: mid=4
   counts += 7//4 = 1
   counts += 5//4 = 2
   counts += 9//4 = 4
   Can obtain. move l=4
End. l=4, r=5: mid=4
```

### Complexity

- Time:  O( n * log range)
    - n = len(ribbons), for loop  judge  canObtainK()
    - range = [0, max(ribbons)]
- Space: O(1)

### Reference:

- [https://leetcode.com/discuss/study-guide/2371234/An-opinionated-guide-to-binary-search-(comprehensive-resource-with-a-bulletproof-template)#33-search-in-rotated-sorted-array](https://leetcode.com/discuss/study-guide/2371234/An-opinionated-guide-to-binary-search-(comprehensive-resource-with-a-bulletproof-template)#33-search-in-rotated-sorted-array)
