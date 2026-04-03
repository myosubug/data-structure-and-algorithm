class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from_left = [1] * len(nums)
        from_right = [1] * len(nums)
        ret = [1] * len(nums)


        for i in range(1, len(nums)):
            from_left[i] = from_left[i-1] * nums[i-1]

        for j in range(len(nums)-2, -1, -1):
            from_right[j] = from_right[j+1] * nums[j+1]
        
        for k in range(len(nums)):
            ret[k] = from_left[k] * from_right[k]

        return ret
