func getLen(node *ListNode) int {
	len := 0
	for node != nil {
		node = node.Next
		len++
	}
	return len
}

func deleteNode(node *ListNode, deleteIndex int) *ListNode {
	if deleteIndex == 0 {
		return node.Next
	}
	head := node
	for deleteIndex != 1 {
		deleteIndex--
		node = node.Next
	}
	node.Next = node.Next.Next
	return head
}

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	len := getLen(head)
	delIdx := len - n
	return deleteNode(head, delIdx)
}
