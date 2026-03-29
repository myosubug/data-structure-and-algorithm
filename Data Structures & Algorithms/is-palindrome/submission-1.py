class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = []
        for ch in s:
            if ch.isalnum():
                stripped.append(ch.lower())
        
        l, r = 0, len(stripped)-1

        for i in range(len(stripped) // 2):
            if stripped[l] != stripped[r]:
                return False
            else:
                l += 1
                r -= 1

        return True
        