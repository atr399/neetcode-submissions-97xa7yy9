class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = 0
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if self.isTarget(nums[mid], target) < 0:
                l = mid + 1
            elif self.isTarget(nums[mid], target) > 0:
                r = mid - 1
            else:
                return mid
        return -1


    def isTarget(self, n, t):
        if n > t:
            return 1
        elif n < t:
            return -1
        else:
            return 0