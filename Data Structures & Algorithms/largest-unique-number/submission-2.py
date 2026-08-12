class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        largest = -1

        for key in counter.keys():
            if counter[key] == 1 and key > largest:
                largest = key

        return largest
