class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0:
            return ""
        
        count_t, window = Counter(t), {}
        have, need = 0, len(count_t)
        ret, minimal = [-1, -1], float('inf')
        left = 0

        for right, c in enumerate(s):
            window[c] = 1 + window.get(c, 0)
            if c in count_t and window[c] == count_t[c]:
                have += 1
            
            while have == need:
                if (right-left+1) < minimal:
                    minimal = (right-left+1)
                    ret = [left, right]
                
                window[s[left]] -= 1
                if s[left] in count_t and window[s[left]] < count_t[s[left]]:
                    have -= 1
                left += 1
        
        l, r = ret

        return s[l:r+1] if minimal != float('inf') else ""