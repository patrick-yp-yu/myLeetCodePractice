# 130. Surrounded Regions
class Solution:
    # Union-Find solution
    # The Os on the borders and the Os that connected to the borders will not be captured.
    # 1. Find all Os that is unioned to the borders. The root set to be a dummy node. 
    # 2. Replace all Os that is not connected to the dummy node.
    # Note that 2D (x,y) is mapping to (x * n + y), n is the column
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:  return
        m, n = len(board), len(board[0])
        union = UnionFind2D(m * n + 1)
        dummy = m * n   # the mapping value for 0s connected to borders
        # Connect 
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    ## AND Nodes that connected to borders
                    if (r == 0 or r == m - 1 or c == 0 or c == n - 1):
                        union.union(dummy, r * n + c)
                    
                    # Check if neighbors = '0' 
                    for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # Up, down, left, right
                        (x,y) = (i+r, j+c)  # the coordinate of neighbor
                        if 0 <= x < m and 0 <= y < n and board[x][y] == 'O':
                            union.union(x * n + y, r * n +c)

        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O' and not union.isUnioned(dummy, r * n + c):
                        board[r][c] = 'X'

        

class UnionFind2D:
    # mapping (r,c) to index 0 ~ r*c -1,  
    # When mapping to value r*c, all the nodes connected to the dummy node
    # Mapping r*c matrix to 1D array
    def __init__(self, dimension:int) -> None:
        self.parent = list(range(dimension))
        self.weight = [0] * (dimension) 
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        else:
            if self.weight[rx] > self.weight[ry]:
                rx, ry = ry, rx     # swap node
            self.parent[rx] = ry
            self.weight[ry] += self.weight[rx]  # count # of connected objects 

    def isUnioned(self, x, y):
        return self.find(x) == self.find(y)               
    # Runtime: 404 ms, faster than 6.23% 
    # Memory Usage: 16.2 MB, less than 13.33%     
