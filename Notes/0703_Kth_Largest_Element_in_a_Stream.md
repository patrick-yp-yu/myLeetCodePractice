# 0703. Kth Largest Element in a Stream

- tag: Heapq, Top-K
- URL: https://leetcode.com/problems/kth-largest-element-in-a-stream/



## Related questions (heapq)

1. HEAP is common data structure to use can be categorized in following 4 categories:
- Top K Pattern
- Merge K Sorted Pattern
- Two Heaps Pattern
- Minimum Number Pattern

## **Top K Pattern**

[LC #215](https://leetcode.com/problems/kth-largest-element-in-an-array/) - Kth largest number in an array. 

[LC #973](https://leetcode.com/problems/k-closest-points-to-origin) - K closest points to origin 

[LC #347](https://leetcode.com/problems/top-k-frequent-elements/) - Top k frequent elements/numbers 

[LC #692](https://leetcode.com/problems/top-k-frequent-words) - Top k frequent words

[LC #264](https://leetcode.com/problems/ugly-number-ii/) - Ugly Number II

[LC #451](https://leetcode.com/problems/sort-characters-by-frequency/) - Frequency Sort 

[LC #703](https://leetcode.com/problems/kth-largest-element-in-a-stream/) - Kth largest number in a stream

[LC #767](https://leetcode.com/problems/reorganize-string/) - Reorganize String

[LC #358](https://leetcode.com/problems/rearrange-string-k-distance-apart) - Rearrange string K distance apart

[LC #1439](https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/) - Kth smallest sum of a matrix with sorted rows

---

## Code1

- python default is a min-heap
- We only keep **k element in the min-heap**
    - ( those numbers < **the k-th largest** ) will be heappop  in the init() function
    - min-heap root = k-th largest element

```python
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k 
        self.pq = nums
        heapq.heapify(self.pq)   # Time:O(n)

        while len(self.pq) > k:  # only keep top-k elements
            heapq.heappop(self.pq)

    def add(self, val: int) -> int:
        heapq.heappush(self.pq, val)    # Time:O(log n)
        if len(self.pq) > self.k:
            heapq.heappop(self.pq)      # Time:O(log n)
        # the min = k-th largest
        return self.pq[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
```

### Complexity

- Time:
    - $O(n \log n + M \log k)$
    - n = len(nums),
    - M = number of add(),
        - heappush() = heappop() = O(log n )
- Space: O(n)

---