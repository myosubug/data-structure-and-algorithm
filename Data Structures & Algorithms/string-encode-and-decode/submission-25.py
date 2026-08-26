class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            ret += "$&*" + s

        return ret

    def decode(self, s: str) -> List[str]:
        spl = s.split("$&*")

        return spl[1:]