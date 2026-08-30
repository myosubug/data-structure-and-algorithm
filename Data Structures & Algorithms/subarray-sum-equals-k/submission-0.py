class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        lookup = {0: 1}
        n = len(nums)
        count = 0
        running_sum = 0
        for n in nums:
            running_sum += n
            count += lookup.get(running_sum - k, 0)
            lookup[running_sum] = lookup.get(running_sum, 0) + 1

        return count