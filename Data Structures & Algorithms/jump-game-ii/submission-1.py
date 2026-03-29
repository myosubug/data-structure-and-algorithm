class Solution:
    def jump(self, nums: List[int]) -> int:
        cache = [float('inf')] * len(nums)
        cache[-1] = 0

        for i in range(len(nums)-2, -1, -1):
            end = min(len(nums), nums[i] + i + 1)
            for j in range(i+1, end):
                cache[i] = min(cache[i], 1 + cache[j])
        
        return cache[0]