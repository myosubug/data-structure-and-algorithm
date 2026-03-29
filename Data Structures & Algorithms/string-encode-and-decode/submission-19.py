class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding =  ""
        for word in strs:
            encoding += word + "@@"
        return encoding
    def decode(self, s: str) -> List[str]:
        split = s.split("@@")
        return split[:-1]