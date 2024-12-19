class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [0] * n
        prefix[0] = nums[0]

        for i in range(1, n):
            prefix[i] = prefix[i-1] + nums[i]
        res = []
        for i in range(n):
            leftSum = prefix[i] - nums[i]
            rightSum = prefix[n-1] - prefix[i]

            leftCnt = i
            rightCnt = n - 1 - i

            leftTotal = leftCnt * nums[i] - leftSum
            rightTotal = rightSum - rightCnt * nums[i]
            res.append(leftTotal + rightTotal)
        return res
