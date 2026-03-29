class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        ret = []

        if not digits:
            return ret

        def helper(path, idx):
            if idx == len(digits):
                ret.append("".join(path.copy()))
                return
            
            for c in digitToChar[digits[idx]]:
                path.append(c)
                helper(path, idx+1)
                path.pop()

        helper([], 0)


        return ret