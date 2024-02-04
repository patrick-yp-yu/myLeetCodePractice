# 0150. Evaluate Reverse Polish Notation

- tag: Stack
- URL: https://leetcode.com/problems/evaluate-reverse-polish-notation/

# Thinking

1. [https://en.wikipedia.org/wiki/Reverse_Polish_notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation)
    1. Reverse Polish notation = postfix notation
    2. `3 4 − 5 +` = `3 − 4 + 5`

### Pseudo code

```python
if t in "+-*/"
		# Do the computation
		# right = op2, it will affect the result of -, / 
else:
		# Put the number into stack
		stack.append( int(t))# convert str to int
```

# Code1

- [https://leetcode.com/problems/evaluate-reverse-polish-notation/discuss/47429/6uff08-132uff09-0-or-1](https://leetcode.com/problems/evaluate-reverse-polish-notation/discuss/47429/6uff08-132uff09-0-or-1)
- Notes:
    - Here, the division is a Round down (truncation) ⇒ int( number1 / number2)
    - int( 6/ (-132)) = 0
    - int(13/5) = 2

```python
import math

num=123.578

# Round to the nearest whole number
print(round(num)) #124

# Round up
print(math.ceil(num)) #124

# Round down
print(math.floor(num)) #123
```

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for i, t in enumerate(tokens):
            if t == '+':
                op_r = int(stack.pop())
                op_l = int(stack.pop())
                stack.append(op_l + op_r)
                # print("{} + {}".format(op_l, op_r), end='   ')
            
            elif t == '-':
                op_r = int(stack.pop())
                op_l = int(stack.pop())
                stack.append(op_l - op_r)
                # print("{} - {}".format(op_l, op_r), end='   ')                
            
            elif t == '*':
                op_r = int(stack.pop())
                op_l = int(stack.pop())
                stack.append(op_l * op_r)
                # print("{} * {}".format(op_l, op_r), end='   ')
                
            elif t == '/':
                op_r = int(stack.pop())
                op_l = int(stack.pop())
                stack.append(int(op_l / op_r)) # truncation = round down
                # print("{} // {}".format(op_l, op_r), end='   ')
            
            # push integers into the stack
            else:
                stack.append(t)
            # print("push {}, {}".format(t, stack))
        
        return stack.pop()
```

```python
input = ["2","1","+","3","*"]

push 2   ['2']
push 1   ['2', '1']
2 + 1   [3]
push 3   [3, '3']
3 * 3   [9]

##############
input = ["4","13","5","/","+"]

push 4   ['4']
push 13   ['4', '13']
push 5   ['4', '13', '5']
13 // 5   ['4', 2]
4 + 2   [6]

##############

input = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

push 10   ['10']
push 6   ['10', '6']
push 9   ['10', '6', '9']
push 3   ['10', '6', '9', '3']
9 + 3   ['10', '6', 12]
push -11   ['10', '6', 12, '-11']
12 * -11   ['10', '6', -132]
6 // -132   ['10', 0]
10 * 0   [0]
push 17   [0, '17']
0 + 17   [17]
push 5   [17, '5']
17 + 5   [22]
```

### Reference:

- [https://gitee.com/programmercarl/leetcode-master/blob/master/problems/0150.逆波兰表达式求值.md](https://gitee.com/programmercarl/leetcode-master/blob/master/problems/0150.%E9%80%86%E6%B3%A2%E5%85%B0%E8%A1%A8%E8%BE%BE%E5%BC%8F%E6%B1%82%E5%80%BC.md)

### Complexity

- Time: O(n)
- Space: O(n)

<br>

# Code2  Optimized code1


```python
##############
    # Optimized
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for i, t in enumerate(tokens):
            
            if t in {'+','-', '*', '/'}:
                op_r = stack.pop()
                op_l = stack.pop()
                if t == '+':
                    stack.append(op_l + op_r)
                elif t == '-':
                    stack.append(op_l - op_r)
                elif t == '*':
                    stack.append(op_l * op_r)
                else:
                    stack.append(int(op_l / op_r)) # truncation = round down
            
            # push integers into the stack
            else:
                stack.append(int(t)) # str to int            
        
        return stack.pop()
```

### Complexity

- Time: O(n)
    - [https://leetcode.com/problems/evaluate-reverse-polish-notation/solution/](https://leetcode.com/problems/evaluate-reverse-polish-notation/solution/)
- Space: O(1) not including the answer. O(n) when included answer

<br>

# Code3

```python
# sol3
    def evalRPN(self, tokens: List[str]) -> int:
        
        def fun(op1, op2, operator):
            if operator == '+':
                return op1 + op2
            if operator == '-':
                return op1 - op2
            if operator == '*':
                return op1 * op2
            if operator == '/':
                return int(op1 / op2)
        
        stack = []
        for t in tokens:
            if t in "+-*/":
                right = stack.pop() # Notice the order !!!
                left = stack.pop()
                stack.append( fun(left, right, t))
            else:
                stack.append(int(t))
        
        return stack[-1]
```

# Extension

Interestingly, this approach could be adapted to work with a **Double-Linked List**. It would require O(n) space to create the list, and then take O(n) time to process it using a similar algorithm to above. 

This works because the algorithm is traversing the list in a linear fashion and modifications only impact the tokens immediately to the left of the current token.