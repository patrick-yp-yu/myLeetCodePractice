import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or not t or not s: 
            return ""
        
        if s == t:
            return t
        
        freq = {}
        for c in t:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        # freq = collections.Counter(t)
        # freq_s = collections.Counter(s)
        # if freq_s == freq:
        #     return t

        begin, end = 0, 0   # define window size
        counter = len(t)
        winSize = len(s)
        ans = ""

        # for end, c in enumerate(s):
        while end < len(s):
            # The char is in string t.
            if s[end] in freq and freq[s[end]] > 0:
                counter -= 1
            freq[s[end]] -= 1

            # print("end={}, {}, counter={}, {}".format(end, s[end], counter, s[begin:end+1]))
            # for item in freq.items():
            #     print(item, end= ' ')
            # print("counter={}".format(counter))
            # Match all substrings. Try to reduce the window
            while counter == 0:
                if end - begin <= winSize:  # Compare window size
                    winSize = end - begin
                    ans = s[begin:end+1]    # include char at index end

                freq[s[begin]] += 1. # Add back to dict
                if s[begin] in freq and freq[s[begin]] > 0:  # Check if s[begin] is in hash
                    counter += 1
                
                # print("Reduce window size:")
                # for item in freq.items():
                #     print(item, end= ' ')
                # print('\n')
                begin += 1

            end += 1
        return ans
            
# test case:
# "ADOBECODEBANC"
# "ABC"
# "a"
# "aa"
# "bb"
# "bb"
# "c"
# "d"
# "ab"
# "A"
# "aaaaaaaaaaaabbbbbcdd"
# "abcd"
# "def"
# "fde"
# "bbaa"
# "aba"

sol1 = Solution()
print(sol1.minWindow("bbaa", "aba"))