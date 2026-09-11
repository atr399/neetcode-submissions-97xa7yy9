class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        HashMap = {}

        for i, n in enumerate(nums):
            remain = target - n

            if remain in HashMap:
                return [HashMap[remain], i]

            HashMap[n] = i

        return -1