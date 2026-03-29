class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        c1 = Counter(s)
        c2 = Counter(t)



        for key, value in c1.items():
            if value != c2[key]:
                return False

        return True