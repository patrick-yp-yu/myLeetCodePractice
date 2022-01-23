# 0455. Assign Cookies
# Yuan-Peng Yu
# 01/22/2022


def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort()
        s.sort()
        
        num_children = len(g)
        
        feeded = 0  # the number of feeded children
        
        for cookie in s:
            if feeded < num_children:   # check if feeded all, 
                if cookie >= g[feeded]:
                    feeded += 1

        return feeded
    # Runtime: 273 ms, faster than 21.19% of Python3
    # Time: O(nlogn), Space: O(n)