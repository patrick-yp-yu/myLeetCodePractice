# 305. Number of Islands II
class Solution:
    # Union Find solution
    # 1. View 2D land as tuple. Use dictinary to play the role of the unique-id array in Union Find.
    # 2. When dictionary is mapping key(tuple) to value(tuple), we do not need m & n.
    # 3. Note that we have to find root(p) & root(q) first so that the rank compaison is valid.
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        root, rank = {}, {}     # root is dict of (tuple

        def addLand(p):
            root[p] = p     # key = tuple, value = tuple
            rank[p] = 1
    
        def find(i):  # Find the root of i
            while i != root[i]:
                root[i] = root[root[i]]
                i = root[i]
            return i 

        def union(p, q):    
            rp = find(p)
            rq = find(q)
            if rp == rq:    return 0
            # Connect smaller tree to larger tree
            if rank[rp] > rank[rq]:   # !!! Use both root to compare rank. 
                rp, rq = rq, rp     # swap
            root[rp] = rq    # p is larger
            rank[rq] += rank[rp]
            return 1    # because 2 connected to 11        

        # positions is mapping into tuple. And, iterate each land
        ans = []
        count = 0
        inPosition = list(map(tuple, positions))
        for p in inPosition:
            # print('Add land={}'.format(p))
            if p not in root:   # Then, add in dict
                addLand(p)
                count += 1
            # p in dict, find the root of p
            i, j = p    # tuple unpacking: i=p[0], j=p[1]
            # DFS: check if neighbors (q) are connected to p's root
            for q in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]: # Up, down, left, right
                if q in root:
                    count -= union(p,q)
                    # print('\tUnion {}/root={} with {}, count={} '.format(p, root[p], q, count))       
            ans.append(count)
        # print(ans)
        return ans  
    # Runtime: 484 ms, faster than 95.33% 
    # Memory Usage: 18.3 MB, less than 25.00%
    ###########################################
## Test case:
# 3
# 3
# [[0,1],[1,2],[2,1],[1,0],[0,2],[0,0],[1,1]]
