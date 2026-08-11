class Solution:
    def confusingNumber(self, n: int) -> bool:
        s = str(n)
        lookup = {
            "0": "0",
            "1": "1",
            "6": "9",
            "8": "8",
            "9": "6"
        }
        
        reverse = s[::-1]
        ret_s = ""
        for k in reverse:
            if k not in lookup:
                return False
            else:
                ret_s += lookup[k]

        
        return True if int(ret_s) != n else False