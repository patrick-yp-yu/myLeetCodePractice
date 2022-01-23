# 3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring_sol1(self, s: str) -> int:
        seenAt = {}     # Stores the last-seen position for a character 
        longest = 0
        start = 0   # the starting pos of a sliding window
        for i, c in enumerate(s):
            # Repeated character, need to update the staring pos
            # seenAt[c] >= start: another repeated char, need update the starting pos 
            # substrings = s[start, i]
            if c in seenAt and seenAt[c] >= start:          
                start = seenAt[c] + 1 # hashmap[c] = index, reset to next index
            # not repeated
            else:   
                longest = max(longest, i - start + 1)   # find the window size
            
            seenAt[c] = i  #(k,v) = (seen char, at index)
            # print("{}, i={}, s={}, l={}".format(c,i, start, longest ))
        return longest
    # Runtime: 40 ms, faster than 99.59%
    # Memory Usage: 13.9 MB, less than 63.93%
    # Time: O(n); Space: O(n)
    
    #######################################
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Size of ASCII table = 256. Use vector to replace the hashmap
        # Record the index of the seen characters. Default = -1 
        seenAt = [-1] * 256

        maxLen, curLen = 0, 0
        start = 0
        for i, c in enumerate(s):
            if seenAt[ord(c)] >= start:  # repeated chars
                start = seenAt[ord(c)] + 1
                curLen = i - start + 1
            else:   # 1st show
                curLen += 1
            seenAt[ord(c)] = i   # update hash to current index
            
            maxLen = max(maxLen, curLen)

        return maxLen
    # Runtime: 60 ms, faster than 75.58%
    # Memory Usage: 14 MB, less than 34.85% 
    
# Test cases:
# "tmmzuxt"