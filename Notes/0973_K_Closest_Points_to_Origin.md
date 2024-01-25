# 0973. K Closest Points to Origin

- tag: Heapq, Top-K
- URL: https://leetcode.com/problems/k-closest-points-to-origin/

## Thinking

1. HEAP is common data structure to use can be categorized in following 4 categories:
- Top K Pattern
- Merge K Sorted Pattern
- Two Heaps Pattern
- Minimum Number Pattern


---

## Code1 heapq

- Find top-k by using heap
- Use `tuples` for heappush, and it will sort by the first element of the tuple:
- distance= sort from small to large
    - the question ask `k-closest points in a list`
    - = heappop() k times

```python
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []

        for x, y in points:
            dist = (x*x + y*y) ** 0.5
            point = [x, y]
            heapq.heappush(pq, (dist, point))
            # print(pq)

        res = []    # save k-closest points
        for _ in range(k):
            res.append(heapq.heappop(pq)[1])
            # print(res)   

        return res
```

```python
points =[[3,3],[5,-1],[-2,4]]
k = 2

pq =
[(4.242640687119285, [3, 3])]
[(4.242640687119285, [3, 3]), (5.0990195135927845, [5, -1])]
[(4.242640687119285, [3, 3]), (5.0990195135927845, [5, -1]), (4.47213595499958, [-2, 4])]

res = 
[[3, 3]]
[[3, 3], [-2, 4]]
```

### Complexity

- Time:
- Space: O(n)

### Python heapq
1. `heapq.heapify(list)`: O(n)
2. `heapq.heappush()`: O(log n)
3. `heapq.heappop()`: O(log n)
4. `heapq.heappushpop()`: O(log n)
5. find min/max, heap[0]: O(1)
6. `heapq.nlargest(n, iterable, key=None)`: O(n log k)
    - where n is the total number of elements in the iterable and 
    - k is the maximum size desired for the returned set.