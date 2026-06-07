class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            ret += s+"1$%^&*1"

        return ret
    def decode(self, s: str) -> List[str]:
        split = s.split("1$%^&*1")
        return split[:-1]
