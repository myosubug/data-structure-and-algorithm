class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        largest = -1

        for n, c in counter.items():
            if c == 1 and n > largest:
                largest = n

        return largest