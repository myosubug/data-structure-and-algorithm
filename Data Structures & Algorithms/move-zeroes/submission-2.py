class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zs = []
        nz = []
        for n in nums:
            if n == 0:
                zs.append(n)
            else:
                nz.append(n)

        merged = nz + zs

        for i in range(len(nums)):
            nums[i] = merged[i]

        # left = 0
        # for right in range(len(nums)):
