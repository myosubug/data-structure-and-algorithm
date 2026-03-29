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

        def helper(i, cur):
            if len(cur) == len(digits):
                ret.append(cur)
                return
            
            for c in digitToChar[digits[i]]:
                helper(i+1, cur+c)
        
        if digits:
            helper(0, "")

        return ret