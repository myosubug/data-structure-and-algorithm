class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted = ""

        for c in s.strip(" "):
            if c.isalnum():
                formatted += c.lower()
        
        return formatted == formatted[::-1]
