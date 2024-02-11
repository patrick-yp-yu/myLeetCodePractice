# Monotonic Stack Pattern

# Find the next greater element in the array
# -1 = not found
def nextGreaterNum(nums):

    stack = []  # save index
    next_greater = [-1] * len(nums)

    for i, num in enumerate(nums):
        # when encounter a larger number
        while stack and nums[stack[-1]] < num:
            small_num_idx = stack.pop()
            next_greater[small_num_idx] = num     
        stack.append(i)
    
    return next_greater

# Find the next smaller element in the array
# -1 = not found
def nextSmallerNum(nums):
    stack = []  # save index
    next_smaller = [-1] * len(nums)

    for i, num in enumerate(nums):
        # when encounter a larger number
        while stack and nums[stack[-1]] > num:
            larger_num_idx = stack.pop()
            next_smaller[larger_num_idx] = num     
        stack.append(i)
    
    return next_smaller

# Find the previous greater element in the array
# -1 = not found
def prevGreaterNum(nums):

    stack = []  # save index
    prev_greater = [-1] * len(nums)

    for i, num in enumerate(nums):
        # continue pop numbers that are <= curr_num
        # => stack only save idx_(number > curr_num ), strictly increasing
        while stack and nums[stack[-1]] <= num:
            stack.pop()
        
        # after while loop, stack only save idx_(number > curr_num )
        if stack:
            prev_greater[i] = nums[stack[-1]]     # index => number
        stack.append(i)
    
    return prev_greater

# Find the previous smaller element in the array
# -1 = not found
def prevSmallerNum(nums):

    stack = []  # save index
    prev_smaller = [-1] * len(nums)

    for i, num in enumerate(nums):
        # continue pop numbers that are >= curr_num
        # => stack only save idx_(number < curr_num ), strictly decreasing
        while stack and nums[stack[-1]] >= num:
            stack.pop()
        
        # after while loop, stack only save idx_(number < curr_num )
        if stack:
            prev_smaller[i] = nums[stack[-1]]     # index => number
        stack.append(i)
    
    return prev_smaller

array = [8, 1, 5, 2, 5, 3, 7, 6, 9]
print(f"array      = {array}")
print(f"nextGreater= {nextGreaterNum(array)}")

print()
print(f"array      = {array}")
print(f"nextSmaller= {nextSmallerNum(array)}")

print()
print(f"array      = {array}")
print(f"prevGreater= {prevGreaterNum(array)}")

print()
print(f"array      = {array}")
print(f"prevSmaller= {prevSmallerNum(array)}")