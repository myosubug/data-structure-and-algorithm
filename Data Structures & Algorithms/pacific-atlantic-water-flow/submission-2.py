class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacifics = set()
        atlantics = set()
        row, col = len(heights), len(heights[0])


        
        # top <-> bottom
        for i in range(col):
            self.dfs(0, i, row, col, heights, pacifics, heights[0][i])
            self.dfs(row-1, i, row, col, heights, atlantics, heights[row-1][i])


        
        # left <-> right
        for j in range(row):
            self.dfs(j, 0, row, col, heights, pacifics, heights[j][0])
            self.dfs(j, col-1, row, col, heights, atlantics, heights[j][col-1])

        ret = []
        for i in range(row):
            for j in range(col):
                if (i,j) in pacifics and (i,j) in atlantics:
                    ret.append([i,j])

        return ret

    def dfs(self, i, j, row, col, heights, seen, prev):
        if (i,j) in seen or not (0 <= i < row) or not (0 <= j < col) or heights[i][j] < prev:
            return

        seen.add((i,j))

        for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
            self.dfs(i+dx, j+dy, row, col, heights, seen, heights[i][j])

        

