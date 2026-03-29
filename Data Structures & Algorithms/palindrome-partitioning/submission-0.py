class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, current_partition):
            if start == len(s):
                res.append(list(current_partition))
                return
    
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if is_palindrome(substring):
                    # Choose, Explore, Un-choose
                    current_partition.append(substring)
                    backtrack(end, current_partition)
                    current_partition.pop()

        backtrack(0, [])

        return res