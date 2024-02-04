# 0020. Valid Parentheses

- tag: Parentheses, Stack
- URL: https://leetcode.com/problems/valid-parentheses/

# Thinking

1. For matching related problem, we should try `stack` first

```python
# 3 situations that does not match
    # 1. Left Extra brackets:  [(){}
    # 2. Right Extra brackets:   (){}]
    # 3. No extra, but mismatch   ([ ) ]
    # Valid => (stack = empty)
```

# Code1

- Compare current character to the`top of the stack` `stack[-1]`  in a for loop
    - if matching parentheses ⇒ stack.pop()
    - if not matching ⇒ return False
- The element in stack = previous appeared chars

```python
# 3 situations that does not match
    # 1. Left Extra brackets:  [(){}
    # 2. Right Extra brackets:   (){}]
    # 3. No extra, but mismatch   ([ ) ]
    # Valid => stack = empty
    def isValid1(self, s: str) -> bool:
        
        stk = []
        for ch in s:

            # Compare stack[-1] & ch. Mismatch => False
            if len(stk) != 0:
                if ch == ')':
                    if stk[-1] == '(':
                        stk.pop()
                        continue
                    else:
                        return False

                if ch == ']':
                    if stk[-1] == '[':
                        stk.pop()
                        continue
                    else:
                        return False
                
                if ch == '}':
                    if stk[-1] == '{':
                        stk.pop()
                        continue
                    else:
                        return False
            stk.append(ch)
            # print("in={}, stack={}".format(ch, stk))
        
        # print("Fianl stack =", stk)

        return len(stk) == 0
```

### Complexity

- Time: O(n)
    - stk.pop() only need O(1)
- Space: O(n)
    - worst case, keep push characters to stack, like `(((((((`


<br>

# Code2

- Here, the element in the stack is different from Code1
- The element in the stack = `the expected char for current char` = `closed bracket`

```python
# pseudo code
for ch in given string: 
		if current char = ‘open bracket’:     # char =      (, [, {
				stack.append(’closed bracket’).   # we expect a ), ], }
		
		else:  # ch = closed bracket 
				if stack exist and brackets are matched
						stack.pop()

				else: # not matched bracket
						return False
		
need to check len(stack) == 0
```

```python
#######
    # Sol2, Use stack
    def isValid_2(self, s: str) -> bool:
            
        stk = []
        for ch in s:
            # open brackets
            if ch == '(':
                stk.append(')')
            elif ch == '[':
                stk.append(']')
            elif ch == '{':
                stk.append('}')

            else: # close brackets or other
                if len(stk) != 0  and ch == stk[-1]:  # matched
                    stk.pop()
                else:
                    return False
        
        return len(stk) == 0
```

### Complexity

- Time: O(n)
- Space: O(n) because of stack

<br>

# Code3

- Similar to Code2. Use a dict to find what stack will append..
    - Use dictionary to simplify the if-sentences

```python
#######
    # Sol3, Use dict
    def isValid(self, s: str) -> bool:

        stk = []
        table = {'(': ')', '[': ']', '{': '}'}
        
        for ch in s:
            # ch = open brackets
            if ch in table:
                stk.append(table[ch]) # append value
            
            # ch = close brackets
            elif len(stk) != 0 and ch == stk[-1]:
                stk.pop()
            
            # other = false
            else:
                return False

        # another way to check "len(stk) == 0"    
        return True if not stk else False
```