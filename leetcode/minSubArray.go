func min(i, j int) int {
    if i < j {
        return i
    }
    return j
}

func minSubArrayLen(target int, nums []int) int {
	var left, right, sumNums
	res := 1001001001

	for right = 0; right < len(nums); right++ {
		sumNums += nums[right]

		for sumNums >= target {
			res = min(res, right - left + 1)
			sumNums -= nums[left]
			left++
		}
	}
	if res == 1001001001 {
		return 0
	} else {
		return res
	}
}
