# 0853. Car Fleet

- tag: Stack
- URL: https://leetcode.com/problems/car-fleet/

## Code1

```python
# pseudo code
traverse reversely, start from the last car
		put into stack
		if stack[-2] >= stack[-1]:
				means the current car(start at smaller pos)= stack[-1]
				already catch up 
				the previous car (start at larger pos)= stack[-2]
				two car merge into the same fleet, 
				stack.pop() current time, because time is decided by the previous car

len(stack) = #of car fleet
```

- pair is sorted by the position;
    - the larger the position, closer to the target
- stack record the time needed to target position
- `stack[-1]` : time needed for the current car (at smaller position)
- `stack[-2]` : time needed for the previours car (at larger position)
- `stack[-2] >= stack[-1]` : less time needed for the current car
    - current car already catch up the previous car,
    - however, cannot surpass, the time & speed will be limited by the previous car. They become the same fleet.
    - Because we use `len(stack)`  to represent the number of fleet.
        - Thus, we keep the time `stack[-2]` for previous car, pop `stack[-1]` for the current car.

```python
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pair = [[p, s] for p, s in zip(position, speed)] # Combine 2 list
        stack = []  # Record the time to target
        
        # Reverse order, large Position first
        # because the speed is decided by the car that is closest to target
        pair = sorted(pair)[::-1]   

        for p, s in pair:
            time = (target - p) / s
            stack.append(time)
            # len(stack) >= 2, a car has caught another one. 
            if len(stack) >=2 and (stack[-2] >= stack[-1]): # need less time
                stack.pop()
        # stack only keep the minimum time
        return len(stack)
        # Time: O(nlogn) because of sorted()
        # Space: O(n) because of pair & stack
```

```python
# list.sort vs sorted(list)
nums = [2, 3, 1, 5, 6, 4, 0]

# sorted() is a function. Need to assign variable to the sorted result. 
print(sorted(nums))   # [0, 1, 2, 3, 4, 5, 6]
print(nums)           # [2, 3, 1, 5, 6, 4, 0]

# list.sort is a method, and sort in-place
print(nums.sort())    # None
print(nums)           # [0, 1, 2, 3, 4, 5, 6]
```



### Complexity

- Time: O(nlogn) because of sorted()
- Space: O(n) because of pair & stack

### Reference:

- [https://www.youtube.com/watch?v=Pr6T-3yB9RM&ab_channel=NeetCode](https://www.youtube.com/watch?v=Pr6T-3yB9RM&ab_channel=NeetCode)