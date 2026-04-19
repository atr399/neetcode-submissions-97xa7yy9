class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # BRUTE FORCE

        res = 0

        for l in range(len(heights)):
            for r in range(l + 1, len(heights)):
                maxArea = (r - l) * min(heights[l], heights[r])
                res = max(res, maxArea)

        return res