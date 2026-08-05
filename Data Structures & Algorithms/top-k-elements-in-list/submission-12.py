class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        result = []

        for num in nums:
            count[num] = 1 + count.get(num, 0)  # count = {1: 1, 2: 2, 3: 3}

        arr = [[] for i in range(len(nums) + 1)]

        for num, cnt in count.items():
            arr[cnt].append(num)                # arr = [[] [1] [2] [3] [] [] []]

        for i in range(len(arr) - 1, 0, -1):
            for n in arr[i]:
                result.append(n)

                if len(result) == k:
                    return result
        