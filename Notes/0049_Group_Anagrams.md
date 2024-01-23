# 0049. Group Anagrams

- tag: HashTable
- URL: https://leetcode.com/problems/group-anagrams/

# Thinking

1. What are the constraints?
    1. strs[i] are lowercase English letters
2. What does output look like?
    1. output = list of list = `[["bat"],["nat","tan"],["ate","eat","tea"]]`
    2. same anagrams are grouped together.

# Notes

- `key = tuple(freq)`  use tuple to become hashable for dict()
- value is a mutable list

# Code

- In the following code, idea is right. However, the `Counter(ch) is unhashable.` Cannot put Counter in a dictionary
- • `strs[i]` consists of lowercase English letters.  (26) ⇒ use array directly

```python
# This code will return "the Counter is unhasable"
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = defaultdict(list) # key = same anagram = same freq counts
        # (key, val) = (frequency,  list)
        for ch in strs:
            
            key = collections.Counter(ch)
            ans[key].append(ch)
            print("(k,v)=({}, {})".format(key, ans[key]))
        
        return ans.values()
```

### Correct code:

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = defaultdict(list) # key = same anagram = same freq counts
        # (key, val) = (frequency,  list)
        for word in strs:
            
            # Find the frequency for each character
            freq = [0] * 26
            for ch in word:
                freq[ ord(ch) - ord("a") ] += 1
            
            key = tuple(freq)       # key  = a 26-elements array
            ans[key].append(word)   # value= list
            print("k={}, v={}".format(key, ans[key]))
        
        return ans.values()
```

- `key = tuple(freq)`  is important step. Turn array into a fixed tuple.
- value = `ans[key]`  is a list. Can append elements.

```python
input = ["eat","tea","tan","ate","nat","bat"]

k=(1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0), v=['eat']
k=(1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0), v=['eat', 'tea']
k=(1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0), v=['tan']
k=(1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0), v=['eat', 'tea', 'ate']
k=(1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0), v=['tan', 'nat']
k=(1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0), v=['bat']
```

# Complexity

word size = k 

- Time:   O(n * word size) = O(n)
    - because the second loop is defined by the size of the word, the word size = a constant
- Space: O(n * k).  The size of dictionary = `n * k`