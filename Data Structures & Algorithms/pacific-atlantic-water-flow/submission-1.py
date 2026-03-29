class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        cols_meet = set()
        rows_meet = set()
        row, col = len(heights), len(heights[0])



        # left -> right
        # right -> left
        for i in range(row):
            self.dfs(i, 0, row, col, cols_meet, heights, heights[i][0])
            self.dfs(i, col-1, row, col, rows_meet, heights, heights[i][col-1])     

        
        # top -> bottom
        # bottom -> top

        for j in range(col):
            self.dfs(0, j, row, col, cols_meet, heights, heights[0][j])
            self.dfs(row-1, j, row, col, rows_meet, heights, heights[row-1][j])
               

        ret = []

        for i in range(row):
            for j in range(col):
                if (i,j) in cols_meet and (i,j) in rows_meet:
                    ret.append([i,j])

        return ret

        
            

    def dfs(self, i, j, row, col, log, heights, prev):
        if (i,j) in log or not(0 <= i < row) or not(0 <= j < col) or heights[i][j] < prev:
            return
        
        log.add((i,j))

        self.dfs(i+1, j, row, col, log, heights, heights[i][j])
        self.dfs(i-1, j, row, col, log, heights, heights[i][j])
        self.dfs(i, j+1, row, col, log, heights, heights[i][j])
        self.dfs(i, j-1, row, col, log, heights, heights[i][j])

