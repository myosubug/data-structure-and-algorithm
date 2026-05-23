class Solution:
    def countElements(self, arr: List[int]) -> int:
        counter = Counter(arr)

        ret = 0
        for n in arr:
            if n+1 in counter:
                ret += 1

        return ret