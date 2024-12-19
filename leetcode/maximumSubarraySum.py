class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        numPositions = defaultdict(list)
        n = len(nums)
        prefix = [0] * (n+1)
        res = -inf+1

        for i, v in enumerate(nums):
            print(i, v-k)
            prefix[i+1] = prefix[i] + nums[i]
            numPositions[v].append(i)
            for pi in numPositions[v-k]:
                res = max(res, prefix[i+1] - prefix[pi])
            for pi in numPositions[v+k]:
                res = max(res, prefix[i+1] - prefix[pi])
        return res if res != -inf+1 else 0
