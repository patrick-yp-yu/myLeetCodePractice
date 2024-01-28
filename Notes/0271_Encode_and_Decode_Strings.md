# 0271. Encode and Decode Strings

- URL: https://leetcode.com/problems/encode-and-decode-strings/

## Thinking

1. `strs[i]` contains any possible characters out of `256` valid ASCII characters.
    - Keypoint: `strs[i]` contains all possible characters, 
    - the key is how we design a **delimiter**



## Code1

- [”left”, “right”, “up”]
    - ⇒ 4$left5$right2$up
    - use `len(word) + $` as a delimiter
- i =  index for traverse each char
- j = counter distance from `(current index)` to  `(the index of delimiter ‘$’)`
    - `s[j]` = the delimiter
    - s[j+1: J+1 + length] = the decoded string
- the task for j:
    1. Record the current index. Need to find the distance from current index to the index of delimiter.
    2. Count + 1 until reach the delimiter
    3. `int(s[i:j]`  parse the length number

```python
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        ### delimiter= len(word)+"$"   4$left 5#right
        res = ""
        for word in strs:
            res = res + str(len(word)) + "$" + word
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        while i < len(s):  # while in-bound
            # Read current index
            j = i 
						
						# count until meeting the delimiter, we can parse "length"
            while s[j] != "$":
                j += 1
            length = int(s[i:j])  # j = pos(delimiter) 

            # find the string 
            res.append(s[j+1: j+1 + length])

            i = j+1 + length    # to traverse next
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
```

```python
str1 = "copyright"
str2 = str[0:4]
>>> str2
'copy'
```

### Complexity

- Time: O(n)
- Space: O(1) when output does not count

---