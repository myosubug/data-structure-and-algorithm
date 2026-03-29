class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = "$12$3$"
        for word in strs:
            ret += word + "$12$3$"
        
        return ret

    def decode(self, s: str) -> List[str]:
        decoded = s.split("$12$3$")

        return decoded[1:-1]