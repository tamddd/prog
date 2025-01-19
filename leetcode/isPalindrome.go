package main

func main() {
	return
}

func isPalindromeIterative(s string) bool {
	left := 0
	right := len(s) - 1

	for left <= right {
		if s[left] != s[right] {
			return false
		}
		left++
		right--
	}
	return true
}
