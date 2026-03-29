class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        pos_diag = set()
        neg_diag = set()
        ret = []

        board = [["."] * n for i in range(n)]

        def helper(r):
            if r == n:
                copy = ["".join(row) for row in board]
                ret.append(copy)
                return

            for c in range(n):
                if c in col or (r+c) in pos_diag or (r-c) in neg_diag:
                    continue
                
                col.add(c)
                pos_diag.add(r+c)
                neg_diag.add(r-c)
                board[r][c] = "Q"
                
                helper(r+1)

                col.remove(c)
                pos_diag.remove(r+c)
                neg_diag.remove(r-c)
                board[r][c] = "."

        helper(0)

        return ret