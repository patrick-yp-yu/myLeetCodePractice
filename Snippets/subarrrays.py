# List all subarrays of a given array:

def getSubarrays(nums):
    # l, r = index of start, end
    ans = []
    for l in range(len(nums)):
        for r in range(l, len(nums)): 
            print(nums[l : r])
            if len(nums[l:r]) != 0:
                ans.append(nums[l : r])    
    return ans
    # Time: O(n^2)

nums1 = [1, 2, 3, 4, 5]
res1 = getSubarrays(nums1)
print(f"subarrays = {res1}")