class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        ret = []
        row, col = len(heights), len(heights[0])

        # pacific to right
        for j in range(col):
            self.helper(0, j, row, col, heights, pac)

        # pacific to down
        for i in range(row):
            self.helper(i, 0, row, col, heights, pac)

        # atl to left
        for y in range(col):
            self.helper(row-1, y, row, col, heights, atl)
        
        # atl to up
        for x in range(row):
            self.helper(x, col-1, row, col, heights, atl)

        for x, y in pac:
            if (x,y) in atl:
                ret.append([x,y])

        return ret


    def helper(self, i, j, row, col, heights, visited):
        if (i, j) in visited:
            return
        visited.add((i, j))
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            ni, nj = i + dx, j + dy
            if (0 <= ni < row) and (0 <= nj < col) and heights[i][j] <= heights[ni][nj]:
                self.helper(ni, nj, row, col, heights, visited)