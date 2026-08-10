class Solution:
    def validWordSquare(self, w: List[str]) -> bool:
        for i in range(len(w)):
            for j in range(len(w[i])):
                if j >= len(w) or i >= len(w[j]) or w[i][j] != w[j][i]:
                    return False

        return True
