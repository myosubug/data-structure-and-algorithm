class Solution:
    def isPalindrome(self, s: str) -> bool:
        updated = ""

        for c in s:
            if c.isalnum():
                updated += c.lower()
        
        l, r = 0, len(updated)-1

        while l <= r:
            if updated[l] != updated[r]:
                return False
            l += 1
            r -= 1
        
        return True