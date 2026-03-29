class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = Counter(s)
        t_counter = Counter(t)

        if len(s_counter.keys()) != len(t_counter.keys()):
            return False

        for k in s_counter.keys():
            if k not in t_counter or s_counter[k] != t_counter[k]:
                return False

        return True