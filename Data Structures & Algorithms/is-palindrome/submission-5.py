class Solution:
    def isPalindrome(self, s: str) -> bool:
        checked = ""

        for c in s:
            if c.isalnum():
                checked += c.lower()
        if len(checked) == 0:
            return True
        left = 0
        right = len(checked) - 1

        while left <= (len(checked) // 2):
            if checked[left] != checked[right]:
                return False
            left += 1
            right -= 1

        return True