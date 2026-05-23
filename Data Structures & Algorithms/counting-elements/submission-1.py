class Solution:
    def countElements(self, arr: List[int]) -> int:
        counter = Counter(arr)

        print(counter)

        ret = 0
        for n in arr:
            if n+1 in counter:
                ret += 1

        return ret