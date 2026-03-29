class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = [False] * len(nums)
        cache[-1] = True

        for i in range(len(nums)-1, -1, -1):
            end = min(len(nums), nums[i] + i + 1)
            print(end)
            for j in range(i+1, end):
                if cache[j]:
                    cache[i] = True
                    break
        return cache[0]