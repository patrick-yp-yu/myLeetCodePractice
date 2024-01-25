# 0347. Top K Frequent Elements

- tag: HashTable, Heapq, Top-K
- URL: https://leetcode.com/problems/top-k-frequent-elements/

<br><br>
# Code1

- 

```python
# Sol1. Use Counter.most_common(k)
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:

        freq = collections.Counter(nums) # (key,val)= number, appearance

        ans = [key for key, val in freq.most_common(k)]
        print(ans)
        return ans
```

### Complexity

- Time: O(n)
- Space: O(n)

<br><br>

# Code2 dict + sort

```python
###################
# Sol3. dict + sort
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
    # 1. find frequence
    freq = defaultdict(int)
    for n in nums:
        freq[n] += 1

    # 2. sort reversely (from max to min)
    sorted_list = sorted(freq.items(), key= lambda item :  -item[1])    # sorted way 1
    # sorted_list = sorted(freq.items(), key= lambda item :  item[1], reverse=True)        # sorted way 2
    ans = [key for key, val in sorted_list ]

    # 3. pick top-k
    return ans[:k]
```

### Complexity

- Time: O(nlog n) because of sorting
- Space: O(n)

<br><br>

# Code3 priority queue

- min heap = a binary tree where parent node value < children value
- Python heapify only takes **O(N)** time  ( swap root to satisfy heap property)
- max_heap = push negative value to min_heap
- Use `tuples` for heappush, and it will sort by the first element of the tuple:


```python
# Sol2.     
    # 1. Count the frequency of each number
    # 2. Sort the frequency
    # 3. Find the first kth
    
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # 1.
        # freq = dict()         # using dict()
        freq = defaultdict(int) # using defaultdict()
        for n in nums:
            # freq[n] = freq.get(n, 0) + 1  # using dict(), default = 0
            freq[n] = freq[n] + 1           # using defaultdict()

        # 2. Sort with heap
        # max_heap = negative value in min_heap
        max_heap = []
        for key, val in freq.items(): # key=number, val = frequence
            heapq.heappush(max_heap, (-val, key)) #  min-heap
            # print("heappush {} {}".format(-val, key))

        ans = []
        for _ in range(k):
            x, key = heapq.heappop(max_heap) # pop the minimum each time
            ans.append(key)
            # print("append {}".format(key))
            
        # print("Final ans =", ans) 
        return ans
```

### Reference:

- [https://python.plainenglish.io/heapify-in-linear-time-114a15487ba1](https://python.plainenglish.io/heapify-in-linear-time-114a15487ba1)
- [https://docs.python.org/3/library/heapq.html](https://docs.python.org/3/library/heapq.html)

### Complexity

- Time: O(n log k)
- Space: O(n + k)

<br><br>
## Heapq: How to use

```python
# To create a heap, you can use the heapify() function. 
# The syntax is:
import heapq

heap = []
heapq.heapify(heap)

# To add an element to the heap, you can use the heappush() function.
heapq.heappush(heap, element)

# Python heapq is a "min heap"
# pop method returns the smallest item
element = heapq.heappop(heap)
```

```python
# Heapsort
def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]

heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

| OPERATION | TIME COMPLEXITY |  | SPACE COMPLEXITY |
| --- | --- | --- | --- |
| Insertion | Best Case: | O(1) | O(1) |
|  | Worst Case: | O(logN) |  |
|  | Average Case: | O(logN) |  |
| Deletion | Best Case: | O(1) | O(1) |
|  | Worst Case: | O(logN) |  |
|  | Average Case: | O(logN) |  |
| Searching | Best Case: | O(1) | O(1) |
|  | Worst Case: | O(N) |  |
|  | Average Case: | O(N) |  |
| Max Value | In MaxHeap: | O(1) | O(1) |
|  | In MinHeap: | O(N) |  |
| Min Value | In MinHeap: | O(1) | O(1) |
|  | In MaxHeap: | O(N) |  |
| Sorting | All Cases: | O(NlogN) | O(1) |
| Creating a Heap | By Inserting all elements: | O(NlogN) | O(N) |
|  | Using Heapify | O(N) | O(1) |