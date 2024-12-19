package main

func max(i, j int) int {
	if i > j {
		return i
	} else {
		return j
	}
}

func maximumSubarraySum(nums []int, k int) int64 {
	numPos := make(map[int][]int)
	var prefix []int
	prefix = append(prefix, 0)
	res := -1 << 52
	for i, v := range nums {
		prefix = append(prefix, prefix[len(prefix)-1]+v)
		numPos[v] = append(numPos[v], i)

		for _, pi := range numPos[v-k] {
			res = max(res, prefix[i+1]-prefix[pi])
		}
		for _, pi := range numPos[v+k] {
			res = max(res, prefix[i+1]-prefix[pi])
		}
	}
	if res != (-1 << 52) {
		return int64(res)
	} else {
		return 0
	}
}
