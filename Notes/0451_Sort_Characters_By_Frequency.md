# 0451. Sort Characters By Frequency

- tag: Heapq
- URL: https://leetcode.com/problems/sort-characters-by-frequency/

---

## Code1

- use min-heap to save (char, freqency)
- output char need to have the same frequency of char

```python
class Solution:
    def frequencySort(self, s: str) -> str:
        
        # Find frequency table
        pq = [(-freq, ch) for ch, freq in Counter(s).items()]
        
        # heapify the list
        heapq.heapify(pq)   # O(n)
        print(pq)
        ans = ""
        while pq:                               # len(pq) = O(n)
            node = heapq.heappop(pq)            # O(log n)
            char, freq = node[1], abs(node[0])
            ans += freq * char
        
        return ans
    # Time: O(n log n), Space: O(n)
```



### Complexity

- Time:O(n log n)
- Space: O(n)


