func largestNumber(nums []int) string {
	sort.Slice(nums, func(i, j int) bool {
		str1 := strconv.Itoa(nums[i])
		str2 := strconv.Itoa(nums[j])
		return str1+str2 > str2+str1
	})

	strNumbers := make([]string, len(nums))
	for i, num := range nums {
		strNumbers[i] = strconv.Itoa(num)
	}

	res := strings.TrimLeft(strings.Join(strNumbers, ""), "0")
    if res == "" {
        res = "0"
    }
	return res
}
