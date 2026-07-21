class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_from_left = [-1] * len(arr)

        for i in range(len(arr)-2, -1, -1):
            max_from_left[i] = max(arr[i+1], max_from_left[i+1])


        return max_from_left