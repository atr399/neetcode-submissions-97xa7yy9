class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # # BRUTE FORCE

        # res = 0

        # for l in range(len(heights)):
        #     for r in range(l + 1, len(heights)):
        #         maxArea = (r - l) * min(heights[l], heights[r])
        #         res = max(res, maxArea)

        # return res

        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            maxArea = (r - l) * min(heights[l], heights[r])
            res = max(res, maxArea)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return res





