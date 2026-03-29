class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = Counter(s)
        c2 = Counter(t)

        if len(c1) > len(c2):
            iterate = c1
            check = c2
        else:
            iterate = c2
            check = c1

        for k in iterate.keys():
            if iterate[k] != check[k]:
                return False
        
        return True