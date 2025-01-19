package main

func main() {
	return
}

type ListNode struct {
	Val  int
	Next *ListNode
}

func isPalindrome(head *ListNode) bool {
	slow, fast := head, head
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}
	var prev *ListNode = nil
	cur := slow
	for cur != nil {
		nex := cur.Next
		cur.Next = prev
		prev = cur
		cur = nex
	}

	first_cur := head
	second_cur := prev

	for first_cur != nil && second_cur != nil {
		if first_cur.Val != second_cur.Val {
			return false
		}
		first_cur = first_cur.Next
		second_cur = second_cur.Next
	}
	return true
}
