class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        vals = []

        for n in nums:
            if n == val:
                continue
            vals.append(n)

        for i in range(len(vals)):
            nums[i] = vals[i]

        return len(vals)
