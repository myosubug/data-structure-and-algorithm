class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0:
            return ""

        count_t, window = Counter(t), {}
        have, need = 0, len(count_t)
        res, minimal = [-1,-1], float('inf')
        left = 0
        for right, c in enumerate(s):
            window[c] = 1 + window.get(c, 0)
            if c in count_t and window[c] == count_t[c]:
                have += 1

            while have == need:
                if (right-left+1) < minimal:
                    res = [left, right]
                    minimal = (right-left+1)
                
                window[s[left]] -= 1
                if s[left] in count_t and window[s[left]] < count_t[s[left]]:
                    have -= 1
                left += 1
        
        l, r = res

        return s[l:r+1] if minimal != float('inf') else ""

        
        
        # if t == "":
        #     return ""

        # countT, window = Counter(t), {}

        # have, need = 0, len(countT)

        # res, min_len = [-1, -1], float('inf')
        # l = 0
        # for r, c in enumerate(s):
        #     window[c] = 1 + window.get(c, 0)

        #     if c in countT and countT[c] == window[c]:
        #         have += 1
            
        #     while have == need:
        #         if (r-l+1) < min_len:
        #             res = [l, r]
        #             min_len = r-l+1
                
        #         window[s[l]] -= 1
        #         if s[l] in countT and window[s[l]] < countT[s[l]]:
        #             have -= 1
        #         l += 1
        
        # l, r = res

        # return s[l:r+1] if min_len != float('inf') else ""