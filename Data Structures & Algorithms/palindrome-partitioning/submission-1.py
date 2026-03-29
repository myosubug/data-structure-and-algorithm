class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret = []


        def helper(path, start):
            if start == len(s):
                ret.append(path.copy())
                return

            for end in range(start+1, len(s)+1):
                part = s[start:end]
                if part == part[::-1]:
                    path.append(part)
                    helper(path, end)
                    path.pop()

        helper([], 0)

        return ret