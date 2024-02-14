# Binary Search

# Template1: find the exact value
# Return the index of the target number. Not found = -1
def binarySearch1(nums, target):

    n = len(nums)
    l, r = 0, n - 1
    while l <= r:
        mid = l + (r - l) // 2

        if (nums[mid] == target):
            return mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    
    return -1    


array = [1, 3, 5, 9, 11]
goal = 5
print(f"array      = {array}")
print(f"Find {goal} at index {binarySearch1(array, goal)}")

# Template2: find a condition (ex: find the min number that > 4)
def binarySearch1(nums, target):
    
    n = len(nums)
    l, r = 0, n-1
    while l < r:        # !!!
        mid = l + (r - l) // 2
        if (nums[mid] < target):
            l = mid + 1
        else:
            r = mid
    
    return l

 