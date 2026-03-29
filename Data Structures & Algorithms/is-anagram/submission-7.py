class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        c1, c2 = Counter(s), Counter(t)

        for k in c1.keys():
            if k not in c2 or c1[k] != c2[k]:
                return False

        return True 