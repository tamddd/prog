func findTargetSumWays(nums []int, target int) int {
    var helper func(nums []int, tot int, idx int) int
    helper = func(nums []int, tot int, idx int) int {
        if len(nums) == idx {
            res := 0
            if tot == 0 {
                res = 1
            }
            return res
        } else {
            return helper(nums, tot-nums[idx], idx+1) + helper(nums, tot+nums[idx], idx+1)
        }
    }
    return helper(nums, target, 0)
}
