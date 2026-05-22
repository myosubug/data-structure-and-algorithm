class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True

        counter = Counter(s)
        single_odd = False
        for k, v in counter.items():
            if v % 2 != 0 and single_odd:
                return False
            elif v % 2 != 0 and not single_odd:
                single_odd = True

        return True