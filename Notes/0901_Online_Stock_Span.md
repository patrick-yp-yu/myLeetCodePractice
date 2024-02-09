# 0901. Online Stock Span

- tag: MonotonicStack
- URL: https://leetcode.com/problems/online-stock-span/

## Thinking

- Find span, span = max consecutive days that price ≤ price_today
    - Including today, so minimum number = 1

```python
Ex1:
previous days=[7,2,1,2], today=[2]
=> span = [2,1,2,2] = 4

Ex2: 
previous days = [7,34,1,2], today =[8]
=> span = [1,2,8] = 3
```

```bash
[100, 80, 60, 70, 60, 75, 85]
To find 85's span, we can reuse 75's span
		75 's span = [60,70,60,75] = 4
        then continue to compare with stack[-1], which is 80
        80's span = 1
        + including today's span = 1 
        => 85's span = 4 + 1 + 1 = 6
        then 85 vs 100, while loop stops
	
```

<br>

## Code1 Monotonic Stack

- Use stack to save price of each day.
    - When `price_today ≥ price_previous`, pop previous element and update span
    - The while loop will stop until `price_today < price_previous`, thus the span cannot grow anymore.

```python
class StockSpanner:

    def __init__(self):
        self.stack = []     # record (price, span)

    def next(self, price: int) -> int:
        span = 1            # including price_today, min = 1
        while self.stack and price >= self.stack[-1][0]:    # when encouter larger price
            span += self.stack.pop()[1]   # span_today will include span_previous

        self.stack.append([price, span])

        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
```

### Complexity

- Time: O(1)= constant,  for each next call
- Space: O(n)
    - worst case, stack grows to size n , [ 5,4,3,2,1]

### Reference:

- [https://www.youtube.com/watch?v=slYh0ZNEqSw](https://www.youtube.com/watch?v=slYh0ZNEqSw)
