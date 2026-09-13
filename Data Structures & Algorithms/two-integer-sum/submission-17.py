class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preMap = {}

        for i, n in enumerate(nums):
            remaining = target - n

            if remaining in preMap:
                return [preMap[remaining], i]

            preMap[n] = i

        return -1