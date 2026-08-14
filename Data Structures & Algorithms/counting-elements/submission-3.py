class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr_set = set(arr)
        counter = 0
        for i in arr:
            if i+1 in arr_set:
                counter += 1

        return counter