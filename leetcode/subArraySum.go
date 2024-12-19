package main

func subarraySum(nums []int, k int) int {
	now := 0
	res := 0
	numCounts := make(map[int]int)
	numCounts[0] = 1
	for _, v := range nums {
		now += v
		res += numCounts[v-k]
		numCounts[v] += 1
	}
	return res
}
