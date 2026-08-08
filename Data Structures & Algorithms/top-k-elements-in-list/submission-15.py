class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []

        count = {}

        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num, cnt in count.items():
            freq[cnt].append(num)

        for i in range(len(freq) - 1, 0, -1):
            for c in freq[i]:
                res.append(c)

                if len(res) == k:
                    return res
