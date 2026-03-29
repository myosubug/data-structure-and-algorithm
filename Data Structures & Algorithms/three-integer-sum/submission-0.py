class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # ret = set()
        # nums.sort()

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 ret.add((nums[i],nums[j],nums[k]))


        # ret = [list(t) for t in ret]
 
        # return ret


        ret = set()
        nums.sort()

        for i in range(len(nums)):
            l, r = i+1, len(nums)-1

            while l < r:
                temp_sum = nums[i] + nums[l] + nums[r]
                if temp_sum > 0:
                    r -= 1
                elif temp_sum < 0:
                    l += 1
                else:
                    ret.add((nums[i],nums[l],nums[r]))
                    l += 1
                    r -= 1

        

        return [list(t) for t in ret]