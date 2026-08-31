class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        counter = 0
        lookup = {0: 1}
        running = 0

        for n in nums:
            running += n
            rem = running % k
            if rem in lookup:
                counter += lookup.get(rem, 0)
            lookup[rem] = lookup.get(rem, 0) + 1

        return counter
            