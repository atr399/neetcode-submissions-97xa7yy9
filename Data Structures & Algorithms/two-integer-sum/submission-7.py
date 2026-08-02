class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIndex = {}

        for i, n in enumerate(nums):
            remain = target - nums[i]
            if remain in numIndex:
                return [numIndex[remain], i]
            numIndex[n] = i

        return -1