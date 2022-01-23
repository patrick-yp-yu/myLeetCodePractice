# 42. Trapping Rain Water

class Solution:
    # Sol1, Monotonic stack
    # Volume = min(left_max, right_max) - each height between left & right
    # Time: O(n)  Space: O(n)
    def trap1(self, height):

        water = 0
        stack = []  # save (index)

        # curr > stack.top, chance to have water 
        for i, curr_h in enumerate(height):
            while stack and curr_h > height[stack[-1]]:
                top_idx = stack.pop()  # pop the smaller height
                if not stack:
                    break
                h = min(curr_h, height[stack[-1]]) - height[top_idx]
                w = i - stack[-1] -1
                water += h * w
                print(f'{i}, currH={curr_h}, {stack},\t ,leftH={height[stack[-1]]}, h*w={h}*{w}, water={water}')
            stack.append(i)
            print(f'{i}, currH={curr_h}, {stack},\t')
        return water 

    # Sol2, Monotonic stack: the stack store (i, height)
    def trap2(self, height):

        water = 0
        stack = [] # store (i, height)
        for i, curr_h in  enumerate(height):
            while stack and curr_h > stack[-1][1]:
                pop_idx, pop_val = stack.pop()
                if not stack: 
                    break
                h = min(curr_h, stack[-1][1]) - pop_val # the smaller height
                w = i - stack[-1][0] -1
                water += h * w
                print(f'{i}, currH={curr_h}, {stack},\t ,leftH={stack[-1][1]}, h*w={h}*{w}, water={water}')
            stack.append((i,curr_h))
            print(f'{i}, currH={curr_h}, {stack},\t')
        return water
    
    #####################
    # Sol3. Two pointer method
    # Time: O(n),  Space: O(1)
    # The water volume is decided by the lower height.
    def trap(self, height):

        l, r = 0, len(height)-1
        l_wall, r_wall = 0, 0
        water = 0 

        while l < r:
            if height[l] < height[r]:  # start from left wall 
                l_wall = max(l_wall, height[l]) # wall must > height
                water += l_wall - height[l]     # water = the height difference
                print(f'l={l}\t wall={l_wall}, h[l]={height[l]}, water={water}')
                l += 1
            else:   # start from right wall
                r_wall = max(r_wall, height[r])
                water += r_wall - height[r]
                print(f'r={r}\t wall={r_wall}, h[r]={height[r]}, water={water}')
                r -= 1
        return water



height1 = [0,1,0,2,1,0,1,3,2,1,2,1] # output = 6
height3 = [1,2,1,3,2,1,2,4,3,2,3,2] # output = 6
height2 = [4,2,0,3,2,5] # output = 9

ans1 = Solution()
print(ans1.trap(height2))

                