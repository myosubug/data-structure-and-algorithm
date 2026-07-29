class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split = s.strip("").split(" ")
        filt = [s for s in split if s != ""]
        return len(filt[-1])