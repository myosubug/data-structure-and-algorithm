class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += "771" + s
        
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = s.split("771")
        return decoded[1:]