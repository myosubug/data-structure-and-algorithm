class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        pac, atl = set(), set()

        for i in range(row):
            self.dfs(i, 0, row, col, pac, heights[i][0], heights)
            self.dfs(i, col-1, row, col, atl, heights[i][col-1], heights)

        for j in range(col):
            self.dfs(0, j, row, col, pac, heights[0][j], heights)
            self.dfs(row-1, j, row, col, atl, heights[row-1][j], heights)

        ret = []

        for i in range(row):
            for j in range(col):
                if (i,j) in pac and (i,j) in atl:
                    ret.append([i,j])
        
        return ret

    def dfs(self, i, j, row, col, visit, prevHeight, heights):
        if (i,j) in visit or not (0 <= i < row) or not (0 <= j < col) or heights[i][j] < prevHeight:
            return

        visit.add((i,j))
        self.dfs(i+1, j, row, col, visit, heights[i][j], heights)
        self.dfs(i-1, j, row, col, visit, heights[i][j], heights)
        self.dfs(i, j+1, row, col, visit, heights[i][j], heights)
        self.dfs(i, j-1, row, col, visit, heights[i][j], heights)