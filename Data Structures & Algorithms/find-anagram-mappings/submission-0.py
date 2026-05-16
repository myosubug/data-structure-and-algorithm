class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []


        m1, m2 = {}, {}

        for i, n in enumerate(nums1):
            m1[n] = i

        for j, m in enumerate(nums2):
            m2[m] = j

        ret = []

        for n in nums1:
            ret.append(m2[n])

        return ret