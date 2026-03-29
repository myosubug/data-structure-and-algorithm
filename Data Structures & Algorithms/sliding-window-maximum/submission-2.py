class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret = []
        left = 0
        right = left + k


        while right <= len(nums):
            temp = nums[left:right]
            ret.append(max(temp))
            left += 1
            right += 1
        
        return ret
            
        