class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            # partition for nums1
            i = (left + right) // 2
            # partition for nums2
            j = (m + n + 1) // 2 - i


            nums1_leftmax = float('-inf') if i == 0 else nums1[i-1]
            nums1_rightmin = float('inf') if i == m else nums1[i]
            nums2_leftmax = float('-inf') if j == 0 else nums2[j-1]
            nums2_rightmin =  float('inf') if j == n else nums2[j]

            if nums1_leftmax <= nums2_rightmin and nums2_leftmax <= nums1_rightmin:
                if (m + n) % 2 == 0:
                    return (max(nums1_leftmax, nums2_leftmax) + min(nums1_rightmin, nums2_rightmin)) / 2
                else:
                    return max(nums1_leftmax,nums2_leftmax)
            elif nums1_leftmax > nums2_rightmin:
                right -= 1
            else:
                left += 1
        
        return -1