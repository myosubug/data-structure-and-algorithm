class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split = s.split(" ")
        for i in reversed(split):
            if i != "":
                return len(i)