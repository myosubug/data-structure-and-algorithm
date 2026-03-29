class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        longest_str = strs[0]
        shortest_str = strs[0]
        lcf = 0

        for s in strs:
            if len(s) > len(longest_str):
                longest_str = s
            elif len(s) < len(shortest_str):
                shortest_str = s
        print(longest_str)
        print(shortest_str)
        for i in range(len(shortest_str)):
            for s in strs:
                if longest_str[i] != s[i]:
                    return shortest_str[:lcf]
            lcf += 1
  
        return shortest_str[:lcf] if lcf >= 1 else ""