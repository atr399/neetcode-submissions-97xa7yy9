class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preMap = {}

        for i, n in enumerate(nums):
            remain = target - n

            if remain in preMap:
                return [preMap[remain], i]

            preMap[n] = i

        return -1