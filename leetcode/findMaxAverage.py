class Solution:
    def findMaxAverage2(self, nums: List[int], k: int) -> float:
        d = [0] * (len(nums) + 1)

        for i in range(1, len(nums)+1):
            d[i] = d[i-1] + nums[i-1]
        ans = -1001001001
        for i in range(k, len(nums)+1):
            ans = max(ans, d[i] - d[i-k])
            print(d[i], d[i-k])
        return ans / k

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum = 0

        for i in range(k):
            cur_sum += nums[i]
        ans = cur_sum

        for i in range(k, len(nums)):
            cur_sum -= nums[i-k]
            cur_sum += nums[i]
            ans = max(ans, cur_sum)
        return ans / k
