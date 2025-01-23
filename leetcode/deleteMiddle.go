func deleteMiddle(head *ListNode) *ListNode {
	if head.Next == nil {
		return nil
	}
	pre := &ListNode{}
	fast := head
	slow := head

	for fast != nil && fast.Next != nil {
		pre = slow
		fast = fast.Next.Next
		slow = slow.Next
	}
	pre.Next = pre.Next.Next
	return head
}
