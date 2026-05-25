class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        ret = [""] * len(s)

        all_move = 0
        for a, b  in shift:
            if a == 0:
                all_move -= b
            else:
                all_move += b

        for i, c in enumerate(s):
            final_shift = (i + all_move) % len(s)
            ret[final_shift]= c
        return "".join(ret)