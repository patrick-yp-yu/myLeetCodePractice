# 0238. Product of Array Except Self

- tag: Array


## Thinking

1. When using division, we just find the total product. Then,
    - `total_product divide nums[i] = product of array except self`


## Code1

- (left product) (i-th) (right product)
    - `product except self = lp[i-1] * rp[i+1]`
- Check left & right boundary
    - left: `ans[0] = rp[1]`
    - right: `ans[n-1] = lp[n-2]`

```python
def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        ans = [1] * n
        lp = [1] * n
        rp = [1] * n

        lp[0] = nums[0]
        for i in range(1, n):
            lp[i] = lp[i-1] * nums[i]

        rp[n-1] = nums[n-1] 
        for i in range(n-2, -1, -1):
            rp[i] = rp[i+1] * nums[i]
        
        print("lp = ", lp)
        print("rp = ", rp)

        # the product except irself
        for i in range(n):
            if i == 0:                  # left boundary
                ans[0] = rp[i+1]
            elif i == n-1:              # right boundary
                ans[n-1] = lp[n-2]
            ### general cases
            else:
                ans[i] = lp[i-1] * rp[i+1]

        return ans
        # Time= O(3n) = O(n), 
        # Space = O(2n) = O(n) because of lp, rp array. The output array does not count.
```

```python
nums =[1, 2, 3, 4]
lp =  [1, 2, 6, 24]
rp = [24, 24, 12, 4]
output=[24,12,8,  6]

########
nums = [-1, 1,  0,-3, 3]
lp =   [-1, -1, 0, 0, 0]
rp =   [0,   0, 0, -9, 3]
output=[0,   0, 9,  0, 0]
```


### Complexity

- Time: O(n)
- Space: O(n)



<br><br>


## Code2 (Better solution)

- Optimize Code1 to improve space complexity
- use variables to record
- Differences:
    - left traverse, ans array record the left product ignore self
    - right travers, ans array multiply to have the right product ignore self
    - We will get answer after traversing both sides
- Notice the boundary

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ans = [1] * len(nums)

        lProduct = 1 
        for i in range(len(nums)):
            ans[i] = lProduct
            lProduct *= nums[i]

        rProduct = 1
        for i in range(len(nums) -1, -1, -1):
            ans[i] *= rProduct
            rProduct *= nums[i]
        
        return ans
```

```python
nums =[1,2,3,4]

nums =[1,2,3,4]

i, ans,      nums[i], lProduct)
0 [1, 1, 1, 1] 1 1
1 [1, 1, 1, 1] 2 2
2 [1, 1, 2, 1] 3 6
3 [1, 1, 2, 6] 4 24

3 [1, 1, 2, 6] 4 4
2 [1, 1, 8, 6] 3 12
1 [1, 12, 8, 6] 2 24
0 [24, 12, 8, 6] 1 24
```

### Reference:

- [https://www.youtube.com/watch?v=bNvIQI2wAjk&ab_channel=NeetCode](https://www.youtube.com/watch?v=bNvIQI2wAjk&ab_channel=NeetCode)
- [https://www.youtube.com/watch?v=gREVHiZjXeQ&ab_channel=Techdose](https://www.youtube.com/watch?v=gREVHiZjXeQ&ab_channel=Techdose)



<br><br>

## Code3

1. find left_product (not include nums[i])
2. find right_product (not include nums[i])
3. product_except_self = left_product * right_product

notes:

- because the product do not include itself,
    - when we compute right product, we start from the 2nd to last.
    - the last product = 1 * nums[the last index]

```python
# Solution left_product * right_product 
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        lp, rp = [1] * n, [1] * n

        # Compute product on left-hand-side
        for i in range(1, n):
            lp[i] = lp[i-1] * nums[i-1]
            # print(i, lp)
        
        print()
        # Compute product on right-hand-side
        # Index starts from 2nd to last
        for i in range(n-2, -1, -1):
            rp[i] = rp[i+1] * nums[i+1]
            # print(i, rp)
        
        # ans = left_product * right_product 
        ans = [lp[i] * rp[i] for i in range(n)]
        return ans
```

```python
nums = [1,2,3,4]

i=1, [1, 1, 1, 1]
i=2, [1, 1, 2, 1]
i=3, [1, 1, 2, 6]

i=2, [1, 1, 4, 1]
i=1, [1, 12, 4, 1]
i=0, [24, 12, 4, 1]

##########
nums =[-1,1,0,-3,3]

i=1, [1, -1, 1, 1, 1]
i=2, [1, -1, -1, 1, 1]
i=3, [1, -1, -1, 0, 1]
i=4, [1, -1, -1, 0, 0]

i=3, [1, 1, 1, 3, 1]
i=2, [1, 1, -9, 3, 1]
i=1, [1, 0, -9, 3, 1]
```

### Optimized Version

- Fine tuned version: only use 1 array

```python
# Optimized Space
    def productExceptSelf_4(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lp =[1] * n
        for i in range(1, n):
            lp[i] = lp[i-1] * nums[i-1]

        r_product = 1
        # Traverse from the last, because we are computing all product
        for i in range(n-1, -1, -1):
            lp[i] = lp[i] * r_product   # r_product at the last = 1
            r_product *= nums[i]        # compute right product

        return lp
```

### Complexity

- Time: O(n)
- Space: O(n)