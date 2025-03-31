package main

func intersection(nums1 []int, nums2 []int) []int {
    var numSets map[int]bool = make(map[int]bool)
    var result map[int]bool = make(map[int]bool)
    var ans []int = make([]int, 0)
    for _, v := range nums1 {
        numSets[v] = true
    }

    for _, v := range nums2 {
        if numSets[v] {
            if !result[v] {
                ans = append(ans, v)
                result[v] = true
            }
        }
    }
    return ans
}
