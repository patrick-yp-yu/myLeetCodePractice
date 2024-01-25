# 0215. Kth Largest Element in an Array

- tag: Heapq, Top-K
- URL: https://leetcode.com/problems/kth-largest-element-in-an-array/description/

## Thinking

1. This question is belong to the `top-k` pattern
    - 703. Kth Largest Element in a Stream

---

## Code1 heapq

- The elements inside priority queue are top-k largest elements,
    - during every iteration, min-heap pop the smallest number
    - pq =[ k-th_max, …, 2nd_max, 1st_max]
    - K-th largest = pq[0]

```python
def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for n in nums:
            # push element
            heapq.heappush(pq, n)               # O(log m), m = heap size
            # print("n={}, pq={}".format(n, pq ))

            # Only need to keep top-k elements in the pq, 
            # Python heap is a min-heap, pop the min.
            if len(pq) > k:
                heapq.heappop(pq)
                # print(">k: ", pq)
        
        return pq[0]
        # Time: O(n log m), m = size(heap), n >> m
        # Space = O(m) because of the heap size
```


### Complexity

- Time:
    - O(n log m), m = size(heap), n >> m
- Space:
    - O(m) because of the heap size

---
<br><br>

## Code2 sort

- 2 ways to reversely sort

```python
# Sorting
    def findKthLargest_v1(self, nums: List[int], k: int) -> int:
        list1 = sorted(nums)
        return list1[-k]
        # Time: O(n logn), Space = O(n) by Timsort algorithm
```

```python
def findKthLargest(self, nums: List[int], k: int) -> int:
				list1 = sorted(nums, reverse=True)
        return list1[k-1]
        # Time: O(n logn), Space = O(n) by Timsort algorithm
```

- need to use `list[k-1]` because of 0-base index


### Complexity

- Time: O(n logn)
- Space: O(n) by Timsort algorithm