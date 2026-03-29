class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True

        reversed_str = str(x)[::-1]
        if negative:
            reversed_str = reversed_str[:-1]
        reversed_int = int(reversed_str)

        if negative:
            reversed_int *= -1

        return reversed_int if pow(-2, 31) <=reversed_int <= pow(2, 31) else 0