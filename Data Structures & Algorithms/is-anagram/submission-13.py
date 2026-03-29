class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s = Counter(s)
        set_t = Counter(t)

        if len(set_s) != len(set_t):
            return False

        for key in set_s.keys():
            if key not in set_t or set_s[key] != set_t[key]:
                return False
        
        return True