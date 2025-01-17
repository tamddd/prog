package main

func removeElement(nums []int, val int) int {
	//slow, fastのpointerで
	//slowがvalじゃない
	slow, fast := 0, 0
	res := 0
	for fast < len(nums) {
		if nums[fast] != val {
			nums[fast], nums[slow] = nums[slow], nums[fast]
			slow++
			res++
		}
		fast++
	}
	return res
}
