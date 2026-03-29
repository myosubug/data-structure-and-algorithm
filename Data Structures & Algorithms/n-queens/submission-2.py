class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posd = set()
        negd = set()

        ret = []

        board = [["."] * n for i in range(n)]

        def helper(row):
            if row == n:
                copy = ["".join(row) for row in board]
                ret.append(copy)
                return

            for c in range(n):
                if c in col or row+c in posd or row-c in negd:
                    continue

                col.add(c)
                posd.add(row+c)
                negd.add(row-c)
                board[row][c] = "Q"

                helper(row+1)

                col.remove(c)
                posd.remove(row+c)
                negd.remove(row-c)
                board[row][c] = "."

        helper(0)

        return ret
        