class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        cand = candidates
        cand.sort()
        ret_set = set()
        path = []

        def helper(target, cur_sum, idx):
            if cur_sum == target:
                ret_set.add(tuple(path.copy()))
                return

            if idx >= len(cand) or cur_sum > target:
                return

            helper(target, cur_sum, idx+1)

            path.append(cand[idx])
            helper(target, cur_sum + cand[idx], idx+1)
            path.pop()

        helper(target, 0, 0)

        

        return [list(s) for s in ret_set]