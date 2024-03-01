# Basic running sum problems

## Type1:

Find the running sum of a given 1D array. For each iteration, add the current number to get the running sum.

## **[1480. Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/description/)**

- Get the running sum.
    
    ```python
    class Solution:
        def runningSum(self, nums: List[int]) -> List[int]:
            
            ans = []
            runningSum = 0 
            for i, x in enumerate(nums):
                runningSum += x
                ans.append(runningSum)
                # print(f"sum={runningSum}    ans={ans}")
            return ans
    ```
    
- Time: O(n); Space: O(1)

## **[1732. Find the Highest Altitude](https://leetcode.com/problems/find-the-highest-altitude/description/)**

- Given`gain` array describes its traveling distance. Try to find the highest altitude.
- Code1: compare `curr_altitude` to `highest` for each iteration
    
    ```python
    class Solution:
        def largestAltitude_1(self, gain: List[int]) -> int:
            
            curr_altitude, highest = 0, 0     # current altitude & highest so far
            
            for i, x in enumerate(gain):
                curr_altitude += x 
                if curr_altitude > highest:
                    highest = curr_altitude
                # print(f"x={x},  curr_altitude={curr_altitude}, highest={highest}")
    
            return highest
    ```
    
- Code2: find the altitude list. Then, get `max(altitude_list)`
    
    ```python
        def largestAltitude(self, gain: List[int]) -> int:
    
            curr_altitude = 0
            altitude_list = [0]         # starts from 0
    
            for i in range(len(gain)):
                curr_altitude += gain[i]
                altitude_list.append(curr_altitude)
            # print(altitude_list)
    
            return max(altitude_list)
    ```
    

## Type2:

Try to compare `left_subarray_sum` to `right_subarray_sum`

## **[724. Find Pivot Index](https://leetcode.com/problems/find-pivot-index/description/)**

## **[1991. Find the Middle Index in Array](https://leetcode.com/problems/find-the-middle-index-in-array/description/)**

- 0724 & 1991 are the same question with different descriptions.
- Trying to find the index that satisfy `left_sum = right_sum`
    - Note that the number at the pivot index is not included in left_sum & right_sum.
- Need to find the total_sum first. Then, we can get  left_sum & right_sum while iterating numbers.
    - right_sum = total_sum - left_sum - x
    - left_sum = the running_sum

```python
class Solution:
    # 1. Find total_sum first, then right_sum = total_sum - left_sum - curr_num
    # 2. Check if left_sum == right_sum:
    # The number at the pivot index is not included in both left_sum & right_sum
    def findMiddleIndex(self, nums: List[int]) -> int:

        
        total_sum = sum(nums)
        left_sum = 0
        for i, x in enumerate(nums):
            right_sum = total_sum - left_sum - x
            if left_sum == right_sum:
                return i

            left_sum += x
        
        return -1        
```

- Time: O(n); Space: O(1)

## **[2270. Number of Ways to Split Array](https://leetcode.com/problems/number-of-ways-to-split-array/description/)**

- Compare left_sum to right_sum.
    - Find the number of split that satisfy`left_sum >= right_sum:`
- Note that there is **at least one** element to the right of `i`. That is, `0 <= i < n - 1`.

```python
class Solution:
    # valid split conditions:
    # 1. left_sum >= right_sum
    # 2. 0 <= i < (n-1)
    def waysToSplitArray(self, nums: List[int]) -> int:
        
        total_sum = sum(nums)
        left_sum = 0
        valid_counts = 0
        n = len(nums)

        for i in range(n - 1):      # 0 <= i < (n-1)
            left_sum += nums[i]
            right_sum = total_sum - left_sum
            if left_sum >= right_sum:
                valid_counts += 1 

        return valid_counts
```

- Time: O(n); Space: O(1)