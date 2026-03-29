class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted = ""
        for c in s:
            if c.isalnum() and c != " ":
                formatted += c.lower()

        return formatted == formatted[::-1]