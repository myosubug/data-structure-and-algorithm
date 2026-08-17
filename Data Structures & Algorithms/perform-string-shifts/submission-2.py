class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        ret = [""] * len(s)
        total = 0

        for di, mo in shift:
            if di == 0:
                total -= mo
            else:
                total += mo
        print(total)
        for i, c in enumerate(s):
            updated = i + total
            if updated < 0:
                updated += len(s)
            new_loc = updated % len(s)
            ret[new_loc] = c

        return "".join(ret)

        