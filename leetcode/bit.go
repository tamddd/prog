package main

import "fmt"

func bit(nums []int) int {
	for i := 0; i < (1 << len(nums)); i++ {
		var subs []int = make([]int, len(nums))
		for j := 0; j < len(nums); j++ {
			if ((i >> j) & 1) == 1 {
				subs = append(subs, nums[j])
			}
		}
		fmt.Println(subs)
	}
	return 90
}
