class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preM = {}

        for i, n in enumerate(nums):
            remain = target - n

            if remain in preM:
                return [preM[remain], i]

            preM[n] = i
