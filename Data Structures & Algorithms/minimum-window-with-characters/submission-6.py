class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = Counter(t)
        have, need  = 0, len(counter)
        minimal = float('inf')
        ret = (-1, -1)
        window = {}
        left = 0

        for right, c in enumerate(s):
            window[c] = window.get(c, 0) + 1
            if c in counter and counter[c] == window[c]:
                have += 1
            
            while have == need:
                if (right-left+1) < minimal:
                    minimal = right-left+1
                    ret = (left, right)
                
                window[s[left]] -= 1
                if s[left] in counter and window[s[left]] < counter[s[left]]:
                    have -= 1
                left += 1
        
        l, r = ret

        return s[l:r+1] if minimal != float('inf') else ""


