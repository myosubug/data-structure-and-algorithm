class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        longest = strs[0]
        shortest = strs[0]
        lcf = 0

        for s in strs:
            if len(s) > len(longest):
                longest = s
            elif len(s) < len(shortest):
                shortest = s

        for i in range(len(shortest)):
            for t in strs:
                if shortest[i] != t[i]:
                    return shortest[:lcf]
            lcf += 1
        
        
        return shortest[:lcf+1] if lcf >= 1 else ""
            


