class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uni = set()

        for n in nums:
            if n in uni:
                return True
            else:
                uni.add(n)

        return False