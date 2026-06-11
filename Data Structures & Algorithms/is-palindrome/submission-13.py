class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        refined_2 = ""
        for c in s:
            if c.isalnum():
                refined_2 += c
        
        refined = refined_2.strip(" ").lower()

        return refined == refined[::-1]