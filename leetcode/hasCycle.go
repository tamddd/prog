func hasCycle(head *ListNode) bool {
    if head == nil {
        return false
    }
	fast := head
	slow := head

	for fast.Next != nil && fast.Next.Next != nil{
		slow = slow.Next
		fast = fast.Next.Next
        if slow == fast {
            return true
        }
	}
	return false
}
