class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}

        for i, n in enumerate(nums):
            remain = target - n

            if remain in Map:
                return [Map[remain], i]

            Map[n] = i

        