class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = Counter(nums)
        index = 0
        for i in range(3):
            occur = counter[i]
            for j in  range(occur):
                nums[index] = i
                index += 1