# 0047. Permutations II

- tag: `Backtracking`
- URL: https://leetcode.com/problems/permutations-ii/

## Thinking

1. In **0047**, the given array contain duplicates.
    - In **0046**, the given numbers in the array are distinct. No duplicates.
2. Because 0047 contains duplicate number, the total number of unique permutations will be ≤ n! 
    
    

<br>

## Code1 Hashmap to record the count of each number

- When choose from candidates in a tree branch, we use a hashmap to find the frequency of each number.
    - `freq = collections.Counter(nums)`
    - (key, value) = (number, counts)
    - if freq. count ≥ 1, we can add this number into path

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
                
        def backtrack():
            
            # Recursion Base case 
            if len(path) == len(nums):      # path = find each permutation
                result.append(path[:])
                # print("     result", result)                
                return 
            
            for k in freq:
                if freq[k] > 0:
                    freq[k] -= 1        # available number -1
                    path.append(k)      
                    
                    # print("k={}, path={}".format(k, path))
                    backtrack()
                       
                    path.pop()          # pop & add back
                    freq[k] += 1
        ###

        result, path = [], []
        # Create a hashmap to record the frequency of numbers
        freq = defaultdict(int)    # k,v = number, frequency
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        # freq = collections.Counter(nums)  # another way
        # print(freq)        
        backtrack()
        return result
```

Running:

```python
defaultdict(<class 'int'>, {1: 2, 2: 1})
k=1, path=[1]
k=1, path=[1, 1]
**k=2, path=[1, 1, 2]
     result [[1, 1, 2]]**
k=2, path=[1, 2]
**k=1, path=[1, 2, 1]
     result [[1, 1, 2], [1, 2, 1]]**
k=2, path=[2]
k=1, path=[2, 1]
**k=1, path=[2, 1, 1]
     result [[1, 1, 2], [1, 2, 1], [2, 1, 1]]**
```

### Complexity

- Time: $O(n \cdot n!)$
    - (Traverse Vertically) Given a set of length `n`, the number of permutations is `n!` . For each path of the tree needs O(n!)
    - (Traverse horizontally) the for loop contribute O(n)
- Space: O(n) for the recursion call stack. The depth of the call stack = len(nums)

### Reference:

- [https://youtu.be/qhBVWf0YafA?si=SpQS2KOe5SnlUcfg](https://youtu.be/qhBVWf0YafA?si=SpQS2KOe5SnlUcfg)

<br>

## Code2 Modified from 0046 code1

- Need to use `nums.sort()`
- Add an extra array `used` to record which element is used.
- To remove duplicate:
    - `i >= 1`, to avoid out of boundary when we try to find `nums[i-1]`
    - `nums[i] == nums[i-1]`: current number is same as the previous one.
    - `used[i-1] == False`: the previous one has performed to find permutation, no need to compute again.
    - When all the conditions are true, we can skip this element.
- `if used[i] == False:` only compute when the element is not used before.

```python
    # Sol2, add a used array to track. Then, remove duplicates.
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def backtrack(nums, path, used):
            # Terminal condition
            if len(path) == len(nums):          # reach leaf node, picked all elements
                result.append(list(path))
                return

            # choose from candidates
            for i in range(len(nums)):

                # Remove duplicate. 
                # At same depth, when the element is same as previous && used[i-1]== False
                # The previous already computed permutations. No need to repeat again.
                if i >= 1 and nums[i] == nums[i-1] and used[i-1] == False:  
                    continue
                    
                if used[i] == False:            # can skip, when the element is used
                    used[i] = True                 # make choice
                    path.append(nums[i])
                    backtrack(nums, path, used)     # recursive
                    path.pop()                      # unmake choice
                    used[i] = False
                    
        ##
        result = []
        **nums.sort()**
        used = [False] * len(nums)
        backtrack(nums, [], used)
        return result
```

### Complexity

- Time: $O(n \cdot n!)$
    - (Traverse Vertically) Given a set of length `n`, the number of permutations is `n!`
    - (Traverse horizontally) the for loop contribute O(n)
- Space: O(n) for the recursion call stack. The depth of the call stack = len(nums)

### Reference:

- [https://gitee.com/programmercarl/leetcode-master/blob/master/problems/0047.全排列II.md](https://gitee.com/programmercarl/leetcode-master/blob/master/problems/0047.%E5%85%A8%E6%8E%92%E5%88%97II.md)