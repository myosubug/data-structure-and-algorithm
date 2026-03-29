class Solution:
    def isPalindrome(self, s: str) -> bool:
        updated_s = ""

        for c in s:
            if c.isalnum():
                updated_s += c.lower()

        l, r = 0, len(updated_s) - 1

        while l <= r:
            if updated_s[l] != updated_s[r]:
                return False
            l += 1
            r -= 1
        
        return True