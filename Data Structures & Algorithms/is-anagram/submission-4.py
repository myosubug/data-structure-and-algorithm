class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_counter = Counter(s)
        t_counter = Counter(t)

        for k in s_counter.keys():
            if s_counter[k] != t_counter[k]:
                return False 

        return True