func removeNodes(head *ListNode) *ListNode {
	revList := reversedList(head)
	max_val := -1001001001

	dummy := &ListNode{Val: -1}
	dummy.Next = revList
	prev := dummy
	cur := revList
	max_val = cur.Val
	for cur != nil {
		if cur.Val < max_val {
			prev.Next = cur.Next
		} else {
			max_val = cur.Val
			prev = cur
		}
		cur = cur.Next
	}
	return reversedList(dummy.Next)
}

func reversedList(head *ListNode) *ListNode {
	var pre *ListNode = nil
	tmp := head
	for tmp != nil {
		nex := tmp.Next
		tmp.Next = pre
		pre = tmp
		tmp = nex
	}
	return pre
}