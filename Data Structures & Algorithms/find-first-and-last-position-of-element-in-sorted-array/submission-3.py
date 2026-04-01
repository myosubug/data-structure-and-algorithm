class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or not target:
            return [-1,-1]
        
        ret = [-1, -1]
        ret[0] = self.searchLeft(nums, target)
        ret[1] = self.searchRight(nums, target)

        if ret[0] == -1 or ret[1] == -1 or nums[ret[0]] != target or nums[ret[1]] != target:
            return [-1,-1]
        return ret  

    def searchRight(self, arr, target):
        left, right = 0, len(arr)-1
        ret = -1

        while left <= right:
            mid = left + (right-left) // 2
            if arr[mid] <= target:
                ret = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ret

    def searchLeft(self, arr, target):
        left, right = 0, len(arr)-1
        ret = -1

        while left <= right:
            mid = left + (right-left) // 2
            if arr[mid] >= target:
                ret = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ret
                