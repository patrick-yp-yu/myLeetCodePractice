# 0560. Subarray Sum Equals K

- tag: `PrefixSum/SubarraySum`
- URL: https://leetcode.com/problems/subarray-sum-equals-k/

# Think 
- A subarray is a contiguous **non-empty** sequence of elements within an array.
    - This is different from subset Sum (DP) problem
    - subarray is contiguous
- sum[0, 6 ] = sum[0,1] + sum[2,6]
- ⇒ sum[2,6] = sum[0,6] - sum[0,1]
- subarraySum = currentSum - prefixSum

Key points：

- If we find out all the subarray, it need O(n^2)
- Directly compute the subarray Sum with the prefix sum method.

<br>

# Sol1: Prefix sum

1. put all currentSum into dictionary, 
2. `currentSum - k = prefix_sum`, look up the prefixSum in dictionary

- k = the target subarraySum = currentSum - prefixSum
- ⇒ prefixSum = currentSum - subarraySum = currentSum - k
- if prefixSum in the dictionary
    - ⇒ subarraySum = k
    - ⇒ counter += seenSum[currentSum -k] , counter records the frequency

```python
class Solution:
    # Using prefix sum and map to find the subarray sum (prefix sum)
    # subarraySum(k) = currentSum - prefixSum(seenSum)  
    def subarraySum_1(self, nums: List[int], k: int) -> int:
        currentSum, counter = 0, 0 
        seenSum = collections.defaultdict(int)   # (k,v) = subarray Sum, 1=seen 
        seenSum[0] = 1  # for currentSum - k = 0  
        
        for x in nums:
            currentSum += x # sum= [0..current]
            
            prefixSum = currentSum - k
            if prefixSum in seenSum:
                counter += seenSum[prefixSum]
            seenSum[currentSum] += 1

        return counter
    # Runtime: 160 ms, faster than 32.41%
    # Memory Usage: 16.3 MB, less than 29.93%
    # Time O(n)
    ########################################
```

Same idea: 

- Different use of dict
- `dict.get(key, 0)` if cannot find key in dict, return 0
- Use `collections.defaultdict()` to avoid missing keys

```python
def subarraySum(self, nums: List[int], k: int) -> int:
        currentSum, counter = 0, 0 
        seenSum = {} # (k,v) = subarray Sum,  
        
        for i,x in enumerate(nums):
            seenSum[currentSum] = seenSum.get(currentSum, 0) + 1
            currentSum += x # sum= [0..current]
            if seenSum.get(currentSum - k):
                counter += seenSum[currentSum - k]
            
            # print("{}: c={}, dic=".format(i, counter), end= ' ')
            # for item in seenSum.items():
            #     print(item, end= ' ')
            # print()
        return counter
    # Runtime: 204 ms, faster than 15.54%
    # Memory Usage: 16.2 MB, less than 46.86%
    ########################################

```

### Complexity

- Time: O(n)
- Space: O(n)

<br>

# code2

![0560_Subarray_Sum_Equals_K.png](/Notes/images/0560_Subarray_Sum_Equals_K.png)

 k  = targetSum = nums[x: y]  (include nums[y] here)

prefix_sum_x = running_sum_x =  the total sum from start (0) to x 

prefix_sum_y = running_sum_x =  the total sum from start (0) to y   

prefix_sum_x =   running_sum_y - targetSum 

```python

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        running_sum = 0
        hash_table = collections.defaultdict(lambda:0)
        total = 0
        for x in nums:
            running_sum += x
            sum = running_sum - k
            if sum in hash_table:
                total += hash_table[sum]
						
						# instead of initialize hash_table[0] = 1
            if running_sum == k: 
                total += 1
            hash_table[running_sum] += 1
        return total
```

<br>

# Code 3


- **whenever sums has `increased by a value of k`, we've found `a subarray of sums=k`.**

```python
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        sums = 0
        d = dict()
        d[0] = 1
        
        for i in range(len(nums)):
            sums += nums[i]
            count += d.get(sums-k,0)
            d[sums] = d.get(sums,0) + 1
        
        return(count)
```

```python
nums = [1,2,1,3] and k = 3

prefix sum = running sum = [0, 1, 3, 4, 7]
k = targetSum = currentSum - prefixSum

Subarray with sum = 3 (k=3)
k = targetSum = currentSum - prefixSum = 3 - 0 = 3
k = targetSum = currentSum - prefixSum = 4 - 1 = 3
k = targetSum = currentSum - prefixSum = 7 - 4 = 3
3 ways
```
### Reference
- [https://leetcode.com/problems/subarray-sum-equals-k/discuss/341399/Python-clear-explanation-with-code-and-example](https://leetcode.com/problems/subarray-sum-equals-k/discuss/341399/Python-clear-explanation-with-code-and-example)

<br>

# Code4

1. curSum = the current running sum 
    1. `if curSum == k:`  current running sum equals target_sum directly, frequency + 1
    2. `if curSum - k in seen:` 
        1. the key in the seen dictionary = prefix_sum for each i
        2. value = the count of prefix sum = the count of target_sum
        3. because `subarray sum(k) = current_sum - prefix_sum`

```python
def subarraySum(self, nums: List[int], k: int) -> int:
        
        curSum, ans = 0, 0
        seen = defaultdict(int) # (prefixSum, frequency)
        
        for i, x in enumerate(nums):
            curSum += x
            
            # instead of initialize seen[0] = 1
            if curSum == k:
                ans += 1
            
            # subarray sum(k) = curSum - prefixSum
            if curSum - k in seen: 
                ans += seen[curSum - k]
            
            seen[curSum] += 1
            # print("{}, curSum={}, curSum-k= {}, ans={}, {},".format(i, curSum, curSum - k, ans, seen))
        return ans

    # Time O(n)

```

running:

```python
[1,2,1,3]
3

0, curSum=1, curSum-k= -2, ans=0, defaultdict(<class 'int'>, {1: 1}),
1, curSum=3, curSum-k= 0, ans=1, defaultdict(<class 'int'>, {1: 1, 3: 1}),
2, curSum=4, curSum-k= 1, ans=2, defaultdict(<class 'int'>, {1: 1, 3: 1, 4: 1}),
3, curSum=7, curSum-k= 4, ans=3, defaultdict(<class 'int'>, {1: 1, 3: 1, 4: 1, 7: 1}),

prefix sum array = [0,1,3,4,7]
# curSum = prefix_sum[current index]
0, curSum=1, curSum-k= -2, ans=0,
1, curSum=3, curSum-k= 0, ans=1, # 
2, curSum=4, curSum-k= 1, ans=2, # 
3, curSum=7, curSum-k= 4, ans=3, # 
```

### Reference

- [https://leetcode.com/problems/subarray-sum-equals-k/discuss/190674/Python-O(n)-Based-on-"running_sum"-concept-of-"Cracking-the-coding-interview"-book](https://leetcode.com/problems/subarray-sum-equals-k/discuss/190674/Python-O(n)-Based-on-%22running_sum%22-concept-of-%22Cracking-the-coding-interview%22-book)