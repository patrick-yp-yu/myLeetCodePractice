# 0078. Subsets

- tag: `Backtracking`
- URL: https://leetcode.com/problems/subsets/

# Related questions

[0090. Subsets II](https://leetcode.com/problems/subsets-ii)

# Thinking

1. **78. Subsets:** each number are unique
2. [90. Subsets II](https://leetcode.com/problems/subsets-ii):  each number can have duplicate

<br>

# Code1 Backtracking

![0078_Subsets.png](/Notes/images/0078_Subsets.png)

- For each branch, 2 decisions: pick/ not pick
- total number of subset = $2^n$, each subset length can up to n
    - total time complexity = $O(n \cdot 2^n)$

```python
# Backtracking
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def dfs(i, path, result):
            # Terminal conditions
            if i >= len(nums):               # Time to return result
                result.append(path.copy())
                return
            
            # 2 choices: pick/not pick current number
            # decision tree pick nums[i]
            path.append(nums[i])
            dfs(i + 1, path, result)
            
            # decision tree NOT to pick nums[i]
            path.pop()
            dfs(i + 1, path, result)

        ######
        result = []
        dfs(0, [], result)
        return result
```

### Reference:

- [https://www.youtube.com/watch?v=REOH22Xwdkk&list=PLot-Xpze53lf5C3HSjCnyFghlW0G1HHXo&index=4](https://www.youtube.com/watch?v=REOH22Xwdkk&list=PLot-Xpze53lf5C3HSjCnyFghlW0G1HHXo&index=4)

### Complexity

- Time: $O(n \cdot 2^n)$
- Space: $O(n \cdot 2^n)$

<br>

# Code2 Tree

- Similar to backtracking,
    - Each time add current node at i
        - children: (i+1)~ len(nums)

```python
def subsets(self, nums: List[int]) -> List[List[int]]:
        #.             []
        #.     [1]       [2]     [3]
        #   [1,2] [1,3]. [2, 3] 
        # [1,2,3]
        ans = []

        def dfs(nums, path):
            # print(f"add path:{path}")
            ans.append(path)
            for i, num in enumerate(nums):
                dfs(nums[i + 1:], path+[num])
        
        dfs(nums, [])
        return ans
```

```python
Input: nums = [1,2,3]

add path:[]
add path:[1]
add path:[1, 2]
add path:[1, 2, 3]
add path:[1, 3]
add path:[2]
add path:[2, 3]
add path:[3]

#####
Input: nums = [0]

add path:[]
add path:[0]
```

<br>

# Code3 Cascade

- Same idea with Code2. Each time add current number
- `l1.extend(l2)`: add all elements in `l2` into the end of `l1`

```python
####
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = [[]]   # already append empty list 
        
        for num in nums:
            r1 = [[num] + x for x in result]    # add current number to each previous result
            result.extend(r1)                   # r1 is a list, use extend to combine 2 list
            print("r1=", r1 )
            print("  result:", result)
        
        return result
```

running:

- start from []
    - add current number to the previous result
    - use list.extend() to add elements into original list

```python
r1= [[1]]
  result: [[], [1]]

# add 2 to each list in the previous result
r1= [[2], [2, 1]]
  result: [[], [1], [2], [2, 1]]

# add 3 to each list in the previous result
r1= [[3], [3, 1], [3, 2], [3, 2, 1]]
  result: [[], [1], [2], [2, 1], [3], [3, 1], [3, 2], [3, 2, 1]]
```

