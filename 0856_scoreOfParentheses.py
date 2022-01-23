# 856. Score of Parentheses


class Solution:
    # Sol1.
    # Need a stack to find the balanced parentheses
    # Time: O(n)  Space: O(n)
    def scoreOfParentheses0(self, s: str) -> int:

        stack = []
        score = 0   # default score 
        
        for i, x in enumerate(s):
            if x == '(':    # Open
                stack.append(score)
                score = 0
            else: # x == ')':  # Close
                score += stack.pop() + max(score, 1)
        
        return score
    
    # Sol2. 
    # Save the score in the stack[-1] 
    # Time: O(n), Space: O(n)
    def scoreOfParentheses(self, s: str) -> int: 
        stack = [0] # Save the score, initial = 0

        for x in s:
            if x == '(':
                stack.append(0)
            else:
                prev_score = stack.pop()        
                stack[-1] += 2 * prev_score or 1
        return stack.pop()
    
    # Sol3


s1 = "()"
s2 = "(())"
s3 = "()()"

sol = Solution()
ans1 = sol.scoreOfParentheses(s1)
print(ans1)
ans2 = sol.scoreOfParentheses(s2)
print(ans2)
ans3 = sol.scoreOfParentheses(s3)
print(ans3)