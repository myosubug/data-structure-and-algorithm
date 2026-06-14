class Solution:
    def wordPattern(self, pattern: str, sss: str) -> bool:
        expected_pattern = {}
        split_sss = sss.split(" ")

        if len(pattern) != len(split_sss):
            return False

        for i in range(len(pattern)):
            print(expected_pattern)
            if pattern[i] in expected_pattern and expected_pattern[pattern[i]] != split_sss[i]:
                return False
            if pattern[i] not in expected_pattern and split_sss[i] in expected_pattern.values():
                return False
            expected_pattern[pattern[i]] = split_sss[i]
        
        return True